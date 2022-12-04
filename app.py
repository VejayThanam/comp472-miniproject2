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

def uniformCostSearch(currentState, sol_file, search_file, puzzleNum, statList):
    # Game is over once car AA (red car) reaches column position 4 (which will occupy col 5 as well)
    start = time.time()
    redCar = currentState.get_red_car()
    visited = []
    stateQueue = {}
    statisticList = [puzzleNum, "UCS", "N/A"]
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
        search_file.write(str(f) + " " + str(g) + " " + str(h) + " " + string_state + "\n") # To print "letter, direction, cost & string game board"

        #checks if redCar is out
        if redCar.col == 4:         
            #Printing Output Information
            end = time.time() #End Runtime
            sol_file.write('\n')
            sol_file.write("Runtime: " + str(end-start)[:5] + " seconds\n")
            sol_file.write("Search path length: " + str(len(visited)) + " states\n")
            sol_file.write("Solution path length: " + str(numMoves) + " moves\n")
            sol_file.write("Solution path: \n")
            statisticList.append(numMoves)
            statisticList.append(len(visited))
            statisticList.append((str(end-start)[:5]))
            #Solution Path
            for move in pathMoveString:
                sol_file.write(move + "\n")
            sol_file.write('\n')
            state.printBoard(sol_file)
            sol_file.write('\n')

            sol_file.write("You WIN!!!!!!!!!\n")
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
            sol_file.write('\n')
            end = time.time() #End Runtime
            sol_file.write("Sorry, could not solve the puzzle as specified.\n")
            sol_file.write("Error: no solution found\n")
            sol_file.write("Runtime: " + str(end-start)[:5] + " seconds\n")
            statisticList.append(numMoves)
            statisticList.append(len(visited))
            statisticList.append((str(end-start)[:5]))
    
    statList.append(statisticList)



def gbfs(currentState, heuristicFunction, sol_file, search_file, puzzleNum, statList):
    start = time.time()
    statisticList = [puzzleNum, "GBFS"]
    closedList = []
    openList = PriorityQueue.PriorityQueue()
    stateQueue = {}
    if heuristicFunction == 'h1':
        heuristic = currentState.getBlockingCars()
        openList.push(heuristic, (0, currentState, "")) # heuristicValue, (numMoves, state, string_move)
        statisticList.append('h1')
    elif heuristicFunction == 'h2':
        heuristic = currentState.getBlockingPositions()
        openList.push(heuristic, (0, currentState, "")) # heuristicValue, (numMoves, state, string_move)
        statisticList.append('h2')
    elif heuristicFunction == 'h3':
        heuristic = currentState.getBlockingPositions() * 3
        openList.push(heuristic, (0, currentState, "")) # heuristicValue, (numMoves, state, string_move)
        statisticList.append('h3')
    else:
        heuristic = currentState.getDistanceToGoal() 
        openList.push(heuristic, (0, currentState, "")) # heuristicValue, (numMoves, state, string_move)
        statisticList.append('h4')
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
        search_file.write(str(f) + " " + str(g) + " " + str(h) + " " + string_state + "\n") # To print "letter, direction, cost & string game board"

         #checks if redCar is out
        if redCar.col == 4:
            #Printing Output Information
            end = time.time() #End Runtime
            statisticList.append(numMoves)
            statisticList.append(len(closedList))
            statisticList.append((str(end-start)[:5]))
            sol_file.write('\n')
            sol_file.write("Runtime: " + (str(end-start)[:5]) + " seconds\n")
            sol_file.write("Search path length: " + str(len(closedList)) + " states\n")
            sol_file.write("Solution path length: " + str(numMoves) + " moves\n")
            sol_file.write("Solution path: \n")
            #Solution Path
            for move in pathMoveString:
                sol_file.write(move + "\n")
            sol_file.write('\n')
            state.printBoard(sol_file)
            sol_file.write('\n')

            sol_file.write("You WIN!!!!!!!!!\n")
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
                    newH = move.getDistanceToGoal()
                if move.get_state_string() not in stateQueue.keys() and move.get_state_string() not in closedList:
                    openList.push(newH, (newNumMoves, move, stringMove))
                    stateQueue[move.get_state_string()] = newH
                    newPath = list(pathMoveString)
                    newPath.append(stringMove)
                    paths.push(newH, (newNumMoves, move, newPath))
            if openList.empty():
                sol_file.write('\n')
                end = time.time() #End Runtime
                statisticList.append(numMoves)
                statisticList.append(len(closedList))
                statisticList.append((str(end-start)[:5]))
                sol_file.write("Sorry, could not solve the puzzle as specified.")
                sol_file.write("Error: no solution found")
                sol_file.write("Runtime: " + (str(end-start)[:5]) + " seconds")

    statList.append(statisticList)
                                                    
def aStar(currentState, heuristicFunction, sol_file, search_file, puzzleNum, statList):
    start = time.time()
    redCar = currentState.get_red_car()
    closedList = []
    stateQueue = {}
    statisticList = [puzzleNum, "A/A*"]
    openList = PriorityQueue.PriorityQueue()
    if heuristicFunction == 'h1':
        heuristic = currentState.getBlockingCars()
        openList.push(heuristic, (0, currentState, "", heuristic)) # heuristicValue, (numMoves, state, string_move)
        statisticList.append('h1')
    elif heuristicFunction == 'h2':
        heuristic = currentState.getBlockingPositions()
        openList.push(heuristic, (0, currentState, "", heuristic)) # heuristicValue, (numMoves, state, string_move)
        statisticList.append('h2')
    elif heuristicFunction == 'h3':
        heuristic = currentState.getBlockingPositions() * 3
        openList.push(heuristic, (0, currentState, "", heuristic)) # heuristicValue, (numMoves, state, string_move)
        statisticList.append('h3')
    else:
        heuristic = currentState.getDistanceToGoal()
        openList.push(heuristic, (0, currentState, "", heuristic)) # heuristicValue, (numMoves, state, string_move)
        statisticList.append('h4')
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
        search_file.write(str(f) + " " + str(g) + " " + str(h) + " " + string_state + "\n") # To print "letter, direction, cost & string game board"

        #checks if redCar is out
        if redCar.col == 4:         
            #Printing Output Information
            end = time.time() #End Runtime
            statisticList.append(numMoves)
            statisticList.append(len(closedList))
            statisticList.append((str(end-start)[:5]))
            sol_file.write('\n')
            sol_file.write("Runtime: " + (str(end-start)[:5]) + " seconds\n")
            sol_file.write("Search path length: " + str(len(closedList)) + " states\n")
            sol_file.write("Solution path length: " + str(numMoves) + " moves\n")
            sol_file.write("Solution path: \n")
            #Solution Path
            for move in pathMoveString:
                sol_file.write(move + "\n")
            sol_file.write('\n')
            state.printBoard(sol_file)
            sol_file.write('\n')

            sol_file.write("You WIN!!!!!!!!!\n")
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
                    newH = move.getDistanceToGoal()
                if move.get_state_string() not in stateQueue.keys() and move.get_state_string() not in closedList:
                    openList.push(newH + newNumMoves, (newNumMoves, move, stringMove, newH))
                    stateQueue[move.get_state_string()] = newH + newNumMoves
                    newPath = list(pathMoveString)
                    newPath.append(stringMove)
                    paths.push(newH + newNumMoves, (newNumMoves, move, newPath, newH))
            if openList.empty():
                sol_file.write('\n')
                end = time.time() #End Runtime
                statisticList.append(numMoves)
                statisticList.append(len(closedList))
                statisticList.append((str(end-start)[:5]))
                sol_file.write("Sorry, could not solve the puzzle as specified.\n")
                sol_file.write("Error: no solution found\n")
                sol_file.write("Runtime: " + (str(end-start)[:5]) + " seconds\n")

    statList.append(statisticList)
        
# Main Function
with open('game_puzzles.txt') as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))
    count=1

    statFile = open("statistics.txt", "w")
    statList = [
        ['Puzzle Number', 'Algorithm', 'Heuristic', 'Length of Solution', 'Length of Search Path', 'Execution Time (s)'],
    ]

    for line in lines:
        if '#' not in line:
            currentState = State.State(line)
            currentState.load_puzzle()

            #UCS
            ucs_sol = open("ucs-sol-" + str(count) + ".txt", "w")
            ucs_sol.write("")
            ucs_sol = open("ucs-sol-" + str(count) + ".txt", "a")

            ucs_search = open("ucs-search-" + str(count) + ".txt", "w")
            ucs_search.write("")
            ucs_search = open("ucs-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            ucs_sol.write("--------------------------------------------------------------------------------\n\n")
            ucs_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(ucs_sol)
            ucs_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(ucs_sol)
            ucs_sol.write('\n')
            uniformCostSearch(currentState, ucs_sol, ucs_search, count, statList)

            #GBFS h1
            gbfs_h1_sol = open("gbfs-h1-sol-" + str(count) + ".txt", "w")
            gbfs_h1_sol.write("")
            gbfs_h1_sol = open("gbfs-h1-sol-" + str(count) + ".txt", "a")

            gbfs_h1_search = open("gbfs-h1-search-" + str(count) + ".txt", "w")
            gbfs_h1_search.write("")
            gbfs_h1_search = open("gbfs-h1-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            gbfs_h1_sol.write("--------------------------------------------------------------------------------\n\n")
            gbfs_h1_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(gbfs_h1_sol)
            gbfs_h1_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(gbfs_h1_sol)
            gbfs_h1_sol.write('\n')
            gbfs(currentState, "h1", gbfs_h1_sol, gbfs_h1_search, count, statList)

            #GBFS h2
            gbfs_h2_sol = open("gbfs-h2-sol-" + str(count) + ".txt", "w")
            gbfs_h2_sol.write("")
            gbfs_h2_sol = open("gbfs-h2-sol-" + str(count) + ".txt", "a")

            gbfs_h2_search = open("gbfs-h2-search-" + str(count) + ".txt", "w")
            gbfs_h2_search.write("")
            gbfs_h2_search = open("gbfs-h2-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            gbfs_h2_sol.write("--------------------------------------------------------------------------------\n\n")
            gbfs_h2_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(gbfs_h2_sol)
            gbfs_h2_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(gbfs_h2_sol)
            gbfs_h2_sol.write('\n')
            gbfs(currentState, "h2", gbfs_h2_sol, gbfs_h2_search, count, statList)

            #GBFS h3
            gbfs_h3_sol = open("gbfs-h3-sol-" + str(count) + ".txt", "w")
            gbfs_h3_sol.write("")
            gbfs_h3_sol = open("gbfs-h3-sol-" + str(count) + ".txt", "a")

            gbfs_h3_search = open("gbfs-h3-search-" + str(count) + ".txt", "w")
            gbfs_h3_search.write("")
            gbfs_h3_search = open("gbfs-h3-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            gbfs_h3_sol.write("--------------------------------------------------------------------------------\n\n")
            gbfs_h3_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(gbfs_h3_sol)
            gbfs_h3_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(gbfs_h3_sol)
            gbfs_h3_sol.write('\n')
            gbfs(currentState, "h3", gbfs_h3_sol, gbfs_h3_search, count, statList)

            #GBFS h4
            gbfs_h4_sol = open("gbfs-h4-sol-" + str(count) + ".txt", "w")
            gbfs_h4_sol.write("")
            gbfs_h4_sol = open("gbfs-h4-sol-" + str(count) + ".txt", "a")

            gbfs_h4_search = open("gbfs-h4-search-" + str(count) + ".txt", "w")
            gbfs_h4_search.write("")
            gbfs_h4_search = open("gbfs-h4-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            gbfs_h4_sol.write("--------------------------------------------------------------------------------\n\n")
            gbfs_h4_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(gbfs_h4_sol)
            gbfs_h4_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(gbfs_h4_sol)
            gbfs_h4_sol.write('\n')
            gbfs(currentState, "h4", gbfs_h4_sol, gbfs_h4_search, count, statList)

            #A Star h1
            aStar_h1_sol = open("aStar-h1-sol-" + str(count) + ".txt", "w")
            aStar_h1_sol.write("")
            aStar_h1_sol = open("aStar-h1-sol-" + str(count) + ".txt", "a")

            aStar_h1_search = open("aStar-h1-search-" + str(count) + ".txt", "w")
            aStar_h1_search.write("")
            aStar_h1_search = open("aStar-h1-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            aStar_h1_sol.write("--------------------------------------------------------------------------------\n\n")
            aStar_h1_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(aStar_h1_sol)
            aStar_h1_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(aStar_h1_sol)
            aStar_h1_sol.write('\n')
            aStar(currentState, "h1", aStar_h1_sol, aStar_h1_search, count, statList)

            #A Star h2
            aStar_h2_sol = open("aStar-h2-sol-" + str(count) + ".txt", "w")
            aStar_h2_sol.write("")
            aStar_h2_sol = open("aStar-h2-sol-" + str(count) + ".txt", "a")

            aStar_h2_search = open("aStar-h2-search-" + str(count) + ".txt", "w")
            aStar_h2_search.write("")
            aStar_h2_search = open("aStar-h2-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            aStar_h2_sol.write("--------------------------------------------------------------------------------\n\n")
            aStar_h2_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(aStar_h2_sol)
            aStar_h2_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(aStar_h2_sol)
            aStar_h2_sol.write('\n')
            aStar(currentState, "h2", aStar_h2_sol, aStar_h2_search, count, statList)

            #A Star h3
            aStar_h3_sol = open("aStar-h3-sol-" + str(count) + ".txt", "w")
            aStar_h3_sol.write("")
            aStar_h3_sol = open("aStar-h3-sol-" + str(count) + ".txt", "a")

            aStar_h3_search = open("aStar-h3-search-" + str(count) + ".txt", "w")
            aStar_h3_search.write("")
            aStar_h3_search = open("aStar-h3-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            aStar_h3_sol.write("--------------------------------------------------------------------------------\n\n")
            aStar_h3_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(aStar_h3_sol)
            aStar_h3_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(aStar_h3_sol)
            aStar_h3_sol.write('\n')
            aStar(currentState, "h3", aStar_h3_sol, aStar_h3_search, count, statList)

            #A Star h4
            aStar_h4_sol = open("aStar-h4-sol-" + str(count) + ".txt", "w")
            aStar_h4_sol.write("")
            aStar_h4_sol = open("aStar-h4-sol-" + str(count) + ".txt", "a")

            aStar_h4_search = open("aStar-h4-search-" + str(count) + ".txt", "w")
            aStar_h4_search.write("")
            aStar_h4_search = open("aStar-h4-search-" + str(count) + ".txt", "a")
            #Printing Inital Board Information 
            aStar_h4_sol.write("--------------------------------------------------------------------------------\n\n")
            aStar_h4_sol.write("Initial Board Configuration: " + str(line) + "\n\n!\n")
            currentState.printBoard(aStar_h4_sol)
            aStar_h4_sol.write("Car Fuel Available: ")
            for car in currentState.cars:
                car.print_initial_carFuel(aStar_h4_sol)
            aStar_h4_sol.write('\n')
            aStar(currentState, "h4", aStar_h4_sol, aStar_h4_search, count, statList)

            count += 1

            


    # firstGame = 'BB.G.HE..G.HEAAG.I..FCCIDDF..I..F...'
    # listOfStates = []

    # currentState = State.State(firstGame)
    # currentState.load_puzzle()

    # listMoves = currentState.get_next_state()

    # for move in listMoves:
    #     move[0].printBoard()

    #Printing Inital Board Information 
    # print("--------------------------------------------------------------------------------")
    # print('\n')
    # print("Initial Board Configuration: ", firstGame)
    # print('\n')
    # print("!")
    # currentState.printBoard()
    # print("Car Fuel Available: ", end=" ")
    # for car in currentState.cars:
    #     car.print_initial_carFuel()
    # print('\n')


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
    

    for row in statList:
        statFile.write("%s\n" % "{: >20} {: >20} {: >20} {: >30} {: >30} {: >30}".format(*row))