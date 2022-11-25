import State
import Car
import string


# First Game Board
# B B . J . .
# . . . J C C
# . A A K . M
# G D D K . M
# G H . . L .
# G H F F L .


with open('sample-input.txt') as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))
    count = 0
    #firstGame = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
    firstGame = 'BBB..MCCDD.MAAKL.MJ.KLEEJ.GG..JHHHII J0 B4'
    listOfStates = []

    currentState = State.State(firstGame)
    currentState.load_puzzle()

    for car in currentState.cars:
        car.print_car()
        print('\n')
           
    # Game is over once car AA (red car) reaches column position 4 (which will occupy col 5 as well)
    redCar = currentState.get_red_car()
    visited = {}
    queue = []
    pathCost = 0
    queue.append((pathCost, currentState, None)) 
    goalReached = False

    while not goalReached and len(queue) > 0:
        #Take out element from front of queue ---> first[0] = cost, first[1] = state
        first = queue.pop(0)
        state = first[1]
        pathCost = first[0]

        #checks if redCar is out
        if redCar.col == 4:
            goalReached = True
            print("You WIN!!!!!!!!!")
            break
        else:
            visited.add(state)
            for move in state.get_next_state():
                # Every move cost 1 Fuel
                moveCost = 1
                newPathCost = pathCost + moveCost

                if move not in queue and move not in visited:
                    queue.append((newPathCost, move, state))
                    redCar = move.get_red_car()
                
                # check if there is shorter path to move
                # elif move in queue:
                #     if pathCost < queue.cost(move)
        
        
        # prints board as a grid
        print("cost: ", pathCost)
        # grid = state.get_state_grid()
        # for i in range(6):
        #     for j in range (6):
        #         print(grid[i][j] + ' ', end="")
        #     print('\n')
        # print('\n')




    # # prints each line of input file
    # for line in lines:
    #     if '#' not in line:
    #         count+=1
    #         print("game ", count)
    #         print(line)


