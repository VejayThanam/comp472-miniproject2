import State
import PriorityQueue
import time 

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

def uniformCostSearchTest(currentState):
    # Game is over once car AA (red car) reaches column position 4 (which will occupy col 5 as well)
    redCar = currentState.get_red_car()
    visited = []
    stateQueue = []
    queue = PriorityQueue.PriorityQueue()
    queue.push(0 ,(currentState, 0, ""))
    stateQueue.append(currentState.get_state_string())

    #Printing Inital Board Information 
    print("--------------------------------------------------------------------------------")
    print('\n')
    print("Initial Board Configuration: ", firstGame)
    print('\n')
    print("!")
    currentState.printBoard()
    print("Car Fuel Available: ", end=" ")
    for car in currentState.cars:
        car.print_initial_carFuel()
    print('\n')

    # Uniform Cost Search
    while not queue.empty():
        #Take out element from front of queue ---> front[0] = cost, front[1] = state
        front = queue.pop()
        stateQueue.pop(0)
        numMoves = front[0]
        state = front[1][0]
        fuelCost = front[1][1]
        string_move=front[1][2]
        redCar = state.get_red_car()
        
        #print(string_move) # To print "letter, direction, cost & string game board"
        print('fuel cost: ', fuelCost)
        print('Number of moves: ', numMoves)
        print("State After board move:")
        state.printBoard()

        #checks if redCar is out
        if redCar.col == 4:
            
            #Printing Output Information
            end = time.time() #End Runtime
            print('\n')
            print("Runtime:",float(str(end-start)[:5]), "seconds")
            print("Search path length: ", len(visited), "states")
            print("Solution path length:", numMoves, "moves")
            print("Solution path: ")
            print('\n')
            print(state.printBoard())
            print('\n')

            print("You WIN!!!!!!!!!")
            break

        visited.append(state.get_state_string())
        for nextMove in state.get_next_state():
            # move contains --> move[0] = state of next move, move[1] = cost of next move
            move = nextMove[0]
            moveCost = nextMove[1]
            stringMove = nextMove[2]
            newNumMoves = numMoves + 1
            newPathCost = fuelCost + moveCost
            if move.get_state_string() not in stateQueue and move.get_state_string() not in visited:
                queue.push(newNumMoves, (move, newPathCost, stringMove))
                stateQueue.append(move.get_state_string())
        if queue.empty():
            print("Sorry, could not solve the puzzle as specified.")
            print("Error: no solution found")
                                
    #print(len(visited))

def uniformCostSearch(currentState):
    # Game is over once car AA (red car) reaches column position 4 (which will occupy col 5 as well)
    redCar = currentState.get_red_car()
    visited = []
    queue = []
    stateQueue = []
    pathCost = 0
    numMoves = 0
    queue.append((pathCost, currentState, None, 0))
    stateQueue.append(currentState.get_state_string())

    # Uniform Cost Search
    while len(queue) > 0:
        #Take out element from front of queue ---> front[0] = cost, front[1] = state
        front = queue.pop(0)
        stateQueue.pop(0)
        pathCost = front[0]
        state = front[1]
        prevState = front[2]
        numMoves = front[3]
        redCar = state.get_red_car()

        print('path cost: ', pathCost)
        print('Number of moves: ', numMoves)
        print("State After board move:")
        state.printBoard()

        #checks if redCar is out
        if redCar.col == 4:
            print("You WIN!!!!!!!!!")
            break

        visited.append(state.get_state_string())
        for nextMove in state.get_next_state():
            # move contains --> move[0] = state of next move, move[1] = cost of next move
            move = nextMove[0]
            moveCost = nextMove[1]
            newNumMoves = numMoves + 1
            newPathCost = pathCost + moveCost
            if prevState != None:
                if move.get_state_string() not in stateQueue and move.get_state_string() not in visited:
                    queue.append((newPathCost, move, state, newNumMoves))
                    stateQueue.append(move.get_state_string())                                 
            else:
                queue.append((newPathCost, move, state, newNumMoves))
                stateQueue.append(move.get_state_string())

    print(len(visited))


# Main Function
with open('sample-input.txt') as f_in:
    start = time.time()
    lines = filter(None, (line.rstrip() for line in f_in))
    count = 0
    firstGame = 'BB.G.HE..G.HEAAG.I..FCCIDDF..I..F...'
    listOfStates = []

    currentState = State.State(firstGame)
    currentState.load_puzzle()

    # Calls uniform cost search      
    #uniformCostSearch(currentState)
    uniformCostSearchTest(currentState)

    # Calls GDBS 

    # Calls A*
    
