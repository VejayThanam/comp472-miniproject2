import State
import Car
import string


# First Game Board
# B B I J . .
# . . I J C C
# . . I A A M
# G D D K . M
# G H . K L .
# G H F F L .


with open('sample-input.txt') as f_in:
    lines = filter(None, (line.rstrip() for line in f_in))
    count = 0
    firstGame = 'BBB..MCCDD.MAAKL.MJ.KLEEJ.GG..JHHHII J0 B4'
    listOfStates = []

    currentState = State.State(firstGame)
    currentState.load_puzzle()

    for car in currentState.cars:
        car.print_car()
        print('\n')

                       

    # Game is over once car AA (red car) reaches column position 4 (which will occupy col 5 as well)
    # redCar = currentState.get_red_car()
    # while redCar.col != 4:
    #     print(currentState.get_state_string())
    #     listOfStates = currentState.get_next_state()
    #     for state in listOfStates:
    #         if state != currentState.prev:
    #             state.prev = currentState
    #             currentState = state
    #             redCar = state.get_red_car()
    #             break

    # print(currentState.get_state_string())

    # for loop
    #     state load puzzle
    #     check next State
    #     assign current state to next State
    #     load puzzle
    #     check next State until state.cars = A [row col] = state.goal


    # # prints each line of input file
    # for line in lines:
    #     if '#' not in line:
    #         count+=1
    #         print("game ", count)
    #         print(line)
