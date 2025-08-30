from domains.wgc import RiverCrossing
from search_core import bfs, ids
import argparse

def print_solution(final_node, stats, algorithm):
    print("Domain: WGC | Algorithm: " + algorithm.upper())
    print(f"Solution cost: {stats.solution_cost} | Depth: {stats.solution_depth}")
    print(f"Nodes generated: {stats.nodes_generated} | Nodes expanded: {stats.nodes_expanded} | Max frontier: {stats.max_frontier}")
    print("Path:")

    path = []
    current = final_node
    while current:
        path.append((current.state, current.action))
        current = current.parent
    path.reverse()

    for i, (state, action) in enumerate(path[1:], 1):
        prev_state = path[i-1][0]
        print(f" {i}) {action:12} ({','.join('LR'[p] for p in prev_state.positions)}) -> ({','.join('LR'[p] for p in state.positions)})")

def main():
    parser = argparse.ArgumentParser(description='Run search algorithms on domains')
    parser.add_argument('--domain', choices=['wgc'], default='wgc', help='Domain to solve')
    parser.add_argument('--algo', choices=['bfs'], default='bfs', help='Algorithm to use')
    args = parser.parse_args()

    if args.domain == 'wgc':
        domain = RiverCrossing()
        if args.algo == 'bfs':
            solution, stats = bfs(domain.initial_state, domain.is_goal, domain.get_successors)
            print_solution(solution, stats)
        else:
            print(f"Algorithm {args.algo} not implemented")
    else:
        print(f"Domain {args.domain} not implemented")

if __name__ == "__main__":
    main()