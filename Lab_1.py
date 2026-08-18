# Problem: Write a python program to formulate AI problem using state space representation.

from collections import deque
def get_next_states(state):
    x, y = state
    next_states = []

    cap1 = 4
    cap2 = 3
    next_states.append((cap1, y))
    next_states.append((x, cap2)) 
    next_states.append((0, y))
    next_states.append((x,0))
    return next_states
initial_state=(0,0)
print("initial state: ",(initial_state))
print("Possible next states: ")
for state in get_next_states(initial_state):
    print(state)