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
    queue.push(0 ,(currentState, 0, ""))
    stateQueue[currentState.get_state_string()] = 0
    paths = PriorityQueue.PriorityQueue()
    paths.push(0 ,(currentState, 0, ""))

    # Uniform Cost Search
    while not queue.empty():
        #Take out element from front of queue ---> front[0] = cost, front[1] = state
        front = queue.pop()
        pathCost = front[0]
        numMoves = front[0]
        state = front[1][0]
        fuelCost = front[1][1]
        string_move=front[1][2]
        redCar = state.get_red_car()

        # print('path cost: ', pathCost)
        path = paths.pop()
        pathMoveString = path[1][2]

        #f(n)
        f = numMoves
        #g(n)
        g = numMoves
        #h(n)
        h = 0
        
        print(string_move) # To print "letter, direction, cost & string game board"
        # print('fuel cost: ', fuelCost)
        # print('Number of moves: ', numMoves)
        # print("State After board move:")
        # state.printBoard()

        #checks if redCar is out
        if redCar.col == 4:         
            #Printing Output Information
            end = time.time() #End Runtime
            print('\n')
            print("Runtime:",float(str(end-start)[:5]), "seconds")
            print("Search path length: ", len(visited), "states")
            print("Solution path length:", numMoves, "moves")
            print("Solution path: ")
            for move in pathMoveString:
                print(move)
            print('\n')
            state.printBoard()
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

                                
            # newPathCost = pathCost + moveCost
            # if move.get_state_string() not in stateQueue.keys() and move.get_state_string() not in visited:
            #     queue.push(newPathCost, (move, newNumMoves))
            #     stateQueue[move.get_state_string()] = newPathCost
            # elif move.get_state_string() in stateQueue.keys():
            #     if newPathCost < stateQueue[move.get_state_string()]:
            #         stateQueue[move.get_state_string()] = newPathCost
            #         queue.push(newPathCost, (move, newNumMoves))
            #     else:
            #         continue

def gbfs(currentState, heuristicFunction):
    closedList = []
    openList = PriorityQueue.PriorityQueue()
    stateQueue = {}
    openList.push(0, (currentState, 0))
    stateQueue[currentState.get_state_string()] = 0
    
    while not openList.empty():
        front = openList.pop()
        state = front[1][0]
        h = front[1][1]
        numMoves = front[0]
        stateQueue.pop(state.get_state_string())
        redCar = state.get_red_car()

        # print('Current Heuristic: ', h)
        # print('Number of moves: ', numMoves)
        # print("State After board move:")
        # state.printBoard()

         #checks if redCar is out
        if redCar.col == 4:
            print("You WIN!!!!!!!!!")
            win(state, closedList, numMoves)
            break
        else:
            closedList.append(state.get_state_string())
            for nextMove in state.get_next_state():
                # move contains --> move[0] = state of next move, move[1] = cost of next move
                move = nextMove[0]
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
                    openList.push(newH, (move, newNumMoves))
                    stateQueue[move.get_state_string()] = newH
                # elif move.get_state_string() in stateQueue.keys():
                #     if newH < stateQueue[move.get_state_string()]:
                #         stateQueue[move.get_state_string()] = newPathCost
                #         queue.push(newPathCost, (move, newNumMoves))
                #     else:
                #         continue
                                                    


# Main Function
with open('sample-input.txt') as f_in:
    start = time.time()
    lines = filter(None, (line.rstrip() for line in f_in))
    count = 0
    firstGame = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
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

    # currentState.printBoard()
    # print('\n')
    
    # listMoves = currentState.get_next_state()

    # for move in listMoves:
    #     move[0].printBoard()

    # Calls uniform cost search      
    uniformCostSearch(currentState)

    # Greedy Best First Search
    # h1 --> Number of blocking Vehicles
    # gbfs(currentState, "h1")
    # h2 --> Number of blocking positions
    # gbfs(currentState, "h2")
    # h3 --> h1 x random constant
    # gbfs(currentState, "h3")
    # h4 --> h2 x random constant
    # gbfs(currentState, "h4")


    # Calls A*
    
# queue = PriorityQueue.PriorityQueue()

# queue.push(34, ("hi", 3))
# queue.push(3, ("hi", 2))
# queue.push(2, ("hi", 1))
# queue.push(32, ("hi", 1))
# queue.push(12, ("hi", 6))

# print(queue.pop())

# queue.push(1, ("hi", 1))

# print(queue.pop())

# queue.push(34, ("hi", 1))

# print(queue.pop())