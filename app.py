import State
import PriorityQueue

# First Game Board
# BBIJ..
# ..IJCC
# ..IAAM
# GDDK.M
# GH.KL.
# GHFFL.

#second game
# ..I...
# BBI.K.
# GHAAKL
# GHDDKL
# G..JEE
# FF.J..


with open('sample-input.txt') as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))
    count = 0
    firstGame = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
    listOfStates = []

    currentState = State.State(firstGame)
    currentState.load_puzzle()

    # Game is over once car AA (red car) reaches column position 4 (which will occupy col 5 as well)
    redCar = currentState.get_red_car()
    visited = []
    queue = []
    stateQueue = []
    pathCost = 0
    queue.append((pathCost, currentState, None))
    stateQueue.append(currentState.get_state_string())
    goalReached = False

    # Uniform Cost Search
    while len(queue) > 0:
        #Take out element from front of queue ---> front[0] = cost, front[1] = state
        front = queue.pop(0)
        stateQueue.pop(0)
        pathCost = front[0]
        state = front[1]
        prevState = front[2]
        redCar = state.get_red_car()

        print('path cost: ', pathCost)
        print("State After board move:")
        state.printBoard()

        #checks if redCar is out
        if redCar.col == 4:
            print("You WIN!!!!!!!!!")
            break

        visited.append(state.get_state_string())
        for move in state.get_next_state():
            # Every move cost 1 Fuel
            moveCost = 1
            newPathCost = pathCost + moveCost
            if prevState != None:
                # if move not in stateQueue and move.get_state_string() != prevState.get_state_string():
                if move.get_state_string() not in stateQueue and move.get_state_string() not in visited:
                    queue.append((newPathCost, move, state))
                    stateQueue.append(move.get_state_string())                                 
            else:
                queue.append((newPathCost, move, state))
                stateQueue.append(move.get_state_string())
                    
    
    print(len(visited))
