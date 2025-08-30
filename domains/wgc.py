from collections import defaultdict, deque

class RiverCrossing:
    def __init__(self):
        self.initial_state = (0,0,0,0)
    
    def is_valid(self, state):
        farmer, wolf, goat, cabbage = state

        # if goat and cabbage are alone
        if farmer != goat and goat == cabbage:
            return False
        
        # if wolf and goat are alone
        if farmer != goat and goat == wolf:
            return False
        
        return True
    
    def get_successors(self, current_state):
        next_states = []
        farmer, wolf, goat, cabbage = current_state

        new_farmer_pos = 1 - farmer

        # farmer moves alone
        possible_state = (new_farmer_pos, wolf, goat, cabbage)
        if self.is_valid(possible_state):
            action = "Return alone" if farmer == 1 else "Go alone"
            next_states.append((possible_state, action))

        # farmer takes wolf
        if farmer == wolf:
            possible_state = (new_farmer_pos, new_farmer_pos, goat, cabbage)
            if self.is_valid(possible_state):
                action = "Return with Wolf" if farmer == 1 else "Move Wolf"
                next_states.append((possible_state, action))

        # farmer takes goat
        if farmer == goat:
            possible_state = (new_farmer_pos, wolf, new_farmer_pos, cabbage)
            if self.is_valid(possible_state):
                action = "Return with Goat" if farmer == 1 else "Move Goat"
                next_states.append((possible_state, action))

        # farmer takes cabbage
        if farmer == cabbage:
            possible_state = (new_farmer_pos, wolf, goat, new_farmer_pos)
            if self.is_valid(possible_state):
                action = "Return with Cabbage" if farmer == 1 else "Move Cabbage"
                next_states.append((possible_state, action))

        return next_states
    
    def is_goal(self, state):
        return all(state)
