from collections import deque

class Node:
    def __init__(self, state, parent=None, action=""):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0 if parent is None else parent.depth + 1

class SearchStats:
    def __init__(self):
        self.nodes_generated = 0
        self.nodes_expanded = 0
        self.max_frontier = 0
        self.solution_cost = 0
        self.solution_depth = 0

# BFS

def bfs(initial_state, goal_test, get_successors):
    stats = SearchStats()
    frontier = deque([Node(initial_state)])
    explored = {initial_state}

    while frontier:
        stats.max_frontier = max(stats.max_frontier, len(frontier))
        node = frontier.popleft()
        stats.nodes_expanded += 1

        if goal_test(node.state):
            stats.solution_cost = node.depth
            stats.solution_depth = node.depth
            return node, stats
        
        for successor_state, action in get_successors(node.state):
            if successor_state not in explored:
                stats.nodes_generated += 1
                explored.add(successor_state)
                frontier.append(Node(successor_state, node, action))

    return None, stats

# IDS

def dfs(initial_state, goal_test, get_successors, depth_limit):
    stats = SearchStats()

    def recursive_dfs(node, depth):
        if depth > depth_limit:
            return None
        
        stats.nodes_expanded += 1

        if goal_test(node.state):
            stats.solution_depth = node.depth
            stats.solution_cost = node.depth
            return node
        
        for successor_state, action in get_successors(node.state):
            stats.nodes_generated += 1
            child = Node(successor_state, node, action)
            result = recursive_dfs(child, depth + 1)
            if result is not None:
                return result
            
        return None
    
    return recursive_dfs(Node(initial_state), 0), stats

def ids(initial_state, goal_test, get_successors):
    stats = SearchStats()
    depth = 0

    while True:
        current_stats = SearchStats()
        result, depth_stats = dfs(initial_state, goal_test, get_successors, depth)

        stats.nodes_generated += depth_stats.nodes_generated
        stats.nodes_expanded += depth_stats.nodes_expanded

        if result is not None:
            stats.solution_depth = depth_stats.solution_depth
            stats.solution_cost = depth_stats.solution_cost
            return result, stats
        
        depth += 1