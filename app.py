import State
import Car


#First Game Board
# B B I J . .
# . . I J C C
# . . I A A M
# G D D K . M
# G H . K L .
# G H F F L .


with open('sample-input.txt') as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))
    count = 0
    firstGame = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
    listOfStates = []

    currentState = State.State(firstGame)
    currentState.load_puzzle()

    redCar = currentState.get_red_car()

    # Game is over once car AA (red car) reaches column position 4 (which will occupy col 5 as well)
    while redCar.col != 4:
        print(currentState.get_state_string())
        listOfStates = currentState.get_next_state()
        for state in listOfStates:
            if state != currentState.prev:
                state.prev = currentState
                currentState = state
                redCar = state.get_red_car()
                break

    print(currentState.get_state_string())   
    
    # for loop
    #     state load puzzle
    #     check next State
    #     assign current state to next State
    #     load puzzle
    #     check next State until state.cars = A [row col] = state.goal

    # listStates = currentState.get_next_state()
    # for state in listStates:
    #     print('\n\n')
    #     grid = state.get_state_grid()
    #     for i in range(6):
    #         for j in range (6):
    #             print(grid[i][j] + ' ', end="")
    #         print('\n')
    #     print('\n\n')

    # for car in s1.cars:
    #     for i in range(6):
    #         for j in range(6):
    #             if car.row==i and car.col==j:
    #                 new_grid[i][j]=car.letter
    #                 if car.horiz and car.length==2:           
    #                         new_grid[i][j+1]=car.letter
    #                 elif car.horiz:
    #                         new_grid[i][j+1]=car.letter
    #                         new_grid[i][j+2]=car.letter
    #                 elif not car.horiz and car.length==2:
    #                     new_grid[i+1][j]=car.letter
    #                 elif not car.horiz:
    #                     new_grid[i+1][j]=car.letter
    #                     new_grid[i+2][j]=car.letter

    # for line in lines:
    #     if '#' not in line:
    #         count+=1
    #         print("game ", count)
    #         s1 = State.State(line)  
    #         s1.load_puzzle(line)
    #         
    #         for state in listOfStates:
    #             print(state.get_state_string())

