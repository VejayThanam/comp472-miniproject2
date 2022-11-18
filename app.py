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

    s1 = State.State(firstGame)
    s1.load_puzzle()

    #s1.get_next_state()

    new_grid = [["." for x in range(6)] for y in range(6)]

    for car in s1.cars:
        car.print_car()
        print('\n')

    for car in s1.cars:
        for i in range(6):
            for j in range(6):
                if car.row==i and car.col==j:
                    new_grid[i][j]=car.letter
                    if car.horiz and car.length==2:           
                            new_grid[i][j+1]=car.letter
                    elif car.horiz:
                            new_grid[i][j+1]=car.letter
                            new_grid[i][j+2]=car.letter
                    elif not car.horiz and car.length==2:
                        new_grid[i+1][j]=car.letter
                    elif not car.horiz:
                        new_grid[i+1][j]=car.letter
                        new_grid[i+2][j]=car.letter

        
    print(new_grid)


    # for state in listOfStates:
    #     print(state.get_state_string())
    #     print(s1.get_state_string())

    # for line in lines:
    #     if '#' not in line:
    #         count+=1
    #         print("game ", count)
    #         s1 = State.State(line)  
    #         s1.load_puzzle(line)
    #         
    #         for state in listOfStates:
    #             print(state.get_state_string())

