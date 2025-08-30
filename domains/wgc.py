from collections import defaultdict, deque

# [0, 0, 0, 0] - initial state
# [1, 0, 1, 0] - Take the goat over 
# [0, 0, 1, 0] - Return empty-handed
# [1, 1, 1, 0] - Take the wolf or cabbage over
# [0, 1, 0, 0] - Return with the goat
# [1, 1, 0, 1] - Take whichever wasn't taken in step 3 over
# [0, 1, 0, 1] - Return empty-handed
# [1, 1, 1, 1] - Take the goat over

# generate a list with each possible move for each step, use BFS or IDS
# determine which results in either goat or cabbage being uneaten
# Initial state (L, L, L, L) -> Move goat (R, L, R, L) -> Return Alone (L, L, R, L) ...

# using a graph

class RiverCrossing:
    def __init__(self):
        self.initial_state = (0,0,0,0)

    def get_state_key(self, state):
        return tuple(state)
    
    def is_valid_state(self, state):
        farmer, wolf, goat, cabbage = state

        # if goat and cabbage are alone
        if farmer != goat and goat == cabbage:
            return False
        
        # if wolf and goat are alone
        if farmer != goat and goat == wolf:
            return False
        
        return True
    
    def get_next_states(self, current_state):
        next_states = []
        farmer, wolf, goat, cabbage = current_state

        new_farmer_pos = 1 - farmer

        # farmer moves alone
        possible_state = [new_farmer_pos, wolf, goat, cabbage]
        if self.is_valid_state(possible_state):
            next_states.append(possible_state)

        # farmer takes wolf
        if farmer == wolf:
            possible_state = [new_farmer_pos, new_farmer_pos, goat, cabbage]
            if self.is_valid_state(possible_state):
                next_states.append(possible_state)

        # farmer takes goat
        if farmer == goat:
            possible_state = [new_farmer_pos, wolf, new_farmer_pos, cabbage]
            if self.is_valid_state(possible_state):
                next_states.append(possible_state)

        # farmer takes cabbage
        if farmer == cabbage:
            possible_state = [new_farmer_pos, wolf, goat, new_farmer_pos]
            if self.is_valid_state(possible_state):
                next_states.append(possible_state)

        return next_states
    
    def is_goal(self, state):
        return all(state)
