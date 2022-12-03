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

def uniformCostSearch(currentState):
    # Game is over once car AA (red car) reaches column position 4 (which will occupy col 5 as well)
    redCar = currentState.get_red_car()
    visited = []
    stateQueue = {}
    queue = PriorityQueue.PriorityQueue()
    queue.push(0 ,(currentState, 0, "")) # numMoves, (state, fuelCost, string_move)
    stateQueue[currentState.get_state_string()] = 0
    paths = PriorityQueue.PriorityQueue() # trace solution path
    paths.push(0 ,(currentState, 0, ""))

    # Uniform Cost Search
    while not queue.empty():
        #Take out element from front of queue ---> front[0] = number of moves, front[1][0] = state of board
        front = queue.pop()
        numMoves = front[0]
        state = front[1][0]
        fuelCost = front[1][1]
        redCar = state.get_red_car()
        visited.append(state.get_state_string())

        string_state = state.get_state_string()

        path = paths.pop()
        pathMoveString = path[1][2]

        #f(n)
        f = numMoves
        #g(n)
        g = numMoves
        #h(n)
        h = 0
        
        #Search Path
        print(str(f) + " " + str(g) + " " + str(h) + " " + string_state) # To print "letter, direction, cost & string game board"

        #checks if redCar is out
        if redCar.col == 4:         
            #Printing Output Information
            end = time.time() #End Runtime
            print('\n')
            print("Runtime:",float(str(end-start)[:5]), "seconds")
            print("Search path length: ", len(visited), "states")
            print("Solution path length:", numMoves, "moves")
            print("Solution path: ")
            #Solution Path
            for move in pathMoveString:
                print(move)
            print('\n')
            state.printBoard()
            print('\n')

            print("You WIN!!!!!!!!!")
            break

        for nextMove in state.get_next_state():
            # move contains --> move[0] = state of next move, move[1] = cost of next move
            move = nextMove[0]
            moveCost = nextMove[1]
            stringMove = nextMove[2]
            newNumMoves = numMoves + 1
            newPathCost = fuelCost + moveCost
            if move.get_state_string() not in stateQueue and move.get_state_string() not in visited:
                queue.push(newNumMoves, (move, newPathCost, stringMove))
                stateQueue[move.get_state_string()] = newPathCost
                newPath = list(pathMoveString)
                newPath.append(stringMove)
                paths.push(newNumMoves, (move, newPathCost, newPath))
        if queue.empty():
            print('\n')
            end = time.time() #End Runtime
            print("Sorry, could not solve the puzzle as specified.")
            print("Error: no solution found")
            print("Runtime:",float(str(end-start)[:5]), "seconds")



def gbfs(currentState, heuristicFunction):
    closedList = []
    openList = PriorityQueue.PriorityQueue()
    stateQueue = {}
    if heuristicFunction == 'h1':
        heuristic = currentState.getBlockingCars()
        openList.push(heuristic, (0, currentState, "")) # heuristicValue, (numMoves, state, string_move)
    elif heuristicFunction == 'h2':
        heuristic = currentState.getBlockingPositions()
        openList.push(heuristic, (0, currentState, "")) # heuristicValue, (numMoves, state, string_move)
    elif heuristicFunction == 'h3':
        heuristic = currentState.getBlockingPositions() * 3
        openList.push(heuristic, (0, currentState, "")) # heuristicValue, (numMoves, state, string_move)
    else:
        heuristic = currentState.getBlockingCars() * 3
        openList.push(heuristic, (0, currentState, "")) # heuristicValue, (numMoves, state, string_move)
    stateQueue[currentState.get_state_string()] = 0
    paths = PriorityQueue.PriorityQueue() # trace solution path
    paths.push(0 ,(currentState, 0, ""))
    
    while not openList.empty():
        front = openList.pop()
        state = front[1][1]
        numMoves = front[1][0]
        stateQueue.pop(state.get_state_string())
        redCar = state.get_red_car()
        closedList.append(state.get_state_string())

        path = paths.pop()
        pathMoveString = path[1][2]

        #f(n)
        f = front[0] 
        #g(n)
        g = 0
        #h(n)
        h = front[0]

        string_state = state.get_state_string()
        
        #Search Path
        print(str(f) + " " + str(g) + " " + str(h) + " " + string_state) # To print "letter, direction, cost & string game board"

         #checks if redCar is out
        if redCar.col == 4:
            #Printing Output Information
            end = time.time() #End Runtime
            print('\n')
            print("Runtime:",float(str(end-start)[:5]), "seconds")
            print("Search path length: ", len(closedList), "states")
            print("Solution path length:", numMoves, "moves")
            print("Solution path: ")
            #Solution Path
            for move in pathMoveString:
                print(move)
            print('\n')
            state.printBoard()
            print('\n')

            print("You WIN!!!!!!!!!")
            break
        else:
            for nextMove in state.get_next_state():
                # move contains --> move[0] = state of next move, move[1] = cost of next move
                move = nextMove[0]
                stringMove = nextMove[2]
                newNumMoves = numMoves + 1
                if heuristicFunction == 'h1':
                    newH = move.getBlockingCars()
                elif heuristicFunction == 'h2':
                    newH = move.getBlockingPositions()
                elif heuristicFunction == 'h3':
                    newH = move.getBlockingPositions() * 3
                else:
                    newH = move.getBlockingCars() * 3
                if move.get_state_string() not in stateQueue.keys() and move.get_state_string() not in closedList:
                    openList.push(newH, (newNumMoves, move, stringMove))
                    stateQueue[move.get_state_string()] = newH
                    newPath = list(pathMoveString)
                    newPath.append(stringMove)
                    paths.push(newH, (newNumMoves, move, newPath))
            if openList.empty():
                print('\n')
                end = time.time() #End Runtime
                print("Sorry, could not solve the puzzle as specified.")
                print("Error: no solution found")
                print("Runtime:",float(str(end-start)[:5]), "seconds")
                                                    
def aStar(currentState, heuristicFunction):
    redCar = currentState.get_red_car()
    closedList = []
    stateQueue = {}
    openList = PriorityQueue.PriorityQueue()
    if heuristicFunction == 'h1':
        heuristic = currentState.getBlockingCars()
        openList.push(heuristic, (0, currentState, "", heuristic)) # heuristicValue, (numMoves, state, string_move)
    elif heuristicFunction == 'h2':
        heuristic = currentState.getBlockingPositions()
        openList.push(heuristic, (0, currentState, "", heuristic)) # heuristicValue, (numMoves, state, string_move)
    elif heuristicFunction == 'h3':
        heuristic = currentState.getBlockingPositions() * 3
        openList.push(heuristic, (0, currentState, "", heuristic)) # heuristicValue, (numMoves, state, string_move)
    else:
        heuristic = currentState.getBlockingCars() * 3
        openList.push(heuristic, (0, currentState, "", heuristic)) # heuristicValue, (numMoves, state, string_move)
    stateQueue[currentState.get_state_string()] = 0
    paths = PriorityQueue.PriorityQueue() # trace solution path
    paths.push(0 ,(currentState, 0, ""))

     # Uniform Cost Search
    while not openList.empty():
        #Take out element from front of queue ---> front[0] = heuristic, front[1][0] = numMoves, front[1][1] = state of board
        front = openList.pop()
        state = front[1][1]
        numMoves = front[1][0]
        redCar = state.get_red_car()
        closedList.append(state.get_state_string())

        string_state = state.get_state_string()

        # print('path cost: ', pathCost)
        path = paths.pop()
        pathMoveString = path[1][2]

        #g(n)
        g = numMoves
        #h(n)
        h = front[1][3]
        #f(n)
        f = g + h
        
        #Search Path
        print(str(f) + " " + str(g) + " " + str(h) + " " + string_state) # To print "letter, direction, cost & string game board"

        #checks if redCar is out
        if redCar.col == 4:         
            #Printing Output Information
            end = time.time() #End Runtime
            print('\n')
            print("Runtime:",float(str(end-start)[:5]), "seconds")
            print("Search path length: ", len(closedList), "states")
            print("Solution path length:", numMoves, "moves")
            print("Solution path: ")
            #Solution Path
            for move in pathMoveString:
                print(move)
            print('\n')
            state.printBoard()
            print('\n')

            print("You WIN!!!!!!!!!")
            break
        else: 
            for nextMove in state.get_next_state():
                move = nextMove[0]
                stringMove = nextMove[2]
                newNumMoves = numMoves + 1
                if heuristicFunction == 'h1':
                    newH = move.getBlockingCars()
                elif heuristicFunction == 'h2':
                    newH = move.getBlockingPositions()
                elif heuristicFunction == 'h3':
                    newH = move.getBlockingPositions() * 3
                else:
                    newH = move.getBlockingCars() * 3
                if move.get_state_string() not in stateQueue.keys() and move.get_state_string() not in closedList:
                    openList.push(newH + newNumMoves, (newNumMoves, move, stringMove, newH))
                    stateQueue[move.get_state_string()] = newH + newNumMoves
                    newPath = list(pathMoveString)
                    newPath.append(stringMove)
                    paths.push(newH + newNumMoves, (newNumMoves, move, newPath, newH))
            if openList.empty():
                print('\n')
                end = time.time() #End Runtime
                print("Sorry, could not solve the puzzle as specified.")
                print("Error: no solution found")
                print("Runtime:",float(str(end-start)[:5]), "seconds")
        


# Main Function
with open('sample-input.txt') as f_in:
    start = time.time()
    lines = filter(None, (line.rstrip() for line in f_in))
    count = 0
    firstGame = 'BB.G.HE..G.HEAAG.I..FCCIDDF..I..F...'
    listOfStates = []

    currentState = State.State(firstGame)
    currentState.load_puzzle()

    listMoves = currentState.get_next_state()

    # for move in listMoves:
    #     move[0].printBoard()

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


    # Calls uniform cost search      
    # uniformCostSearch(currentState)

    # Greedy Best First Search
    # h1 --> Number of blocking Vehicles
    # gbfs(currentState, "h1")
    # h2 --> Number of blocking positions
    # gbfs(currentState, "h2")
    # h3 --> h1 x random constant
    # gbfs(currentState, "h3")
    # h4 --> h2 x random constant
    # gbfs(currentState, "h4")


    # A* Algorithm
    # h1 --> Number of blocking Vehicles
    # aStar(currentState, "h1")
    # h2 --> Number of blocking positions
    # aStar(currentState, "h2")
    # h3 --> h1 x random constant
    # aStar(currentState, "h3")
    # h4 --> h2 x random constant
    # aStar(currentState, "h4")
    