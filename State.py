import Car

# Define State class (state of the game board)
class State:
    def __init__(self, line):
        self.N = 6  # size of board
        self.cars = []  # num of cars
        self.goal = [2, 5]  # end goal
        self.prev = None  # previous state
        self.puzzle = line

    # Makes copy of current state of the board
    def cloneState(self):
        s = State(self.puzzle)
        s.N = self.N
        for c in self.cars:
            s.cars.append(Car.Car(c.row, c.col, c.length, c.horiz, c.letter))
        s.goal = self.goal.copy()
        s.puzzle = self.puzzle
        return s

    # Load puzzle using file
    def load_puzzle(self):
        count = 0
        grid = [[0 for x in range(self.N)] for y in range(self.N)] 

        # places puzzle in a 2x2 grid
        for i in range(self.N):
            for j in range(self.N):
                grid[i][j] = self.puzzle[count]
                count += 1
        
        # retrieves length of each car in puzzle
        puzzle=''.join(self.puzzle)          
        length = {}
        for i in puzzle: 
            if i != '.':
                if i in length: 
                    length[i]=length[i] + 1
                else: 
                    length[i] = 1

        # finds position (row, col) of each car
        carList = {}
        for i in range(self.N):
            for j in range(self.N):
                if grid[i][j] not in carList and grid[i][j] != '.':
                        if j == 0:
                            if grid[i][j]==grid[i][j+1]:
                                carList[grid[i][j]] = [i, j, length[grid[i][j]], True]
                            else:
                                carList[grid[i][j]] = [i, j, length[grid[i][j]], False]
                        elif j == 5:
                            if grid[i][j]==grid[i][j-1]:
                                carList[grid[i][j]] = [i, j, length[grid[i][j]], True]
                            else:
                                carList[grid[i][j]] = [i, j, length[grid[i][j]], False]
                        else:
                            if grid[i][j]==grid[i][j-1] or grid[i][j]==grid[i][j+1]:
                                carList[grid[i][j]] = [i, j, length[grid[i][j]], True]
                            else:
                                carList[grid[i][j]] = [i, j, length[grid[i][j]], False]
       
        for car in carList:
            # print(car)
            # print("row:", carList[car][0], " col:", carList[car][1], " length:", carList[car][2], " horizontal:", carList[car][3])
            self.cars.append(Car.Car(carList[car][0], carList[car][1], carList[car][2], carList[car][3], car))

    # Return state of board as String
    def get_state_string(self):
        s = ""
        grid = self.get_state_grid()
        str = sum(grid, [])
        s = ''.join(str)
        return s

    # Returns NxN 2-D Matrix of State
    def get_state_grid(self):
        # grid = [[-1]*self.N for i in range(self.N)]
        # print(grid)
        # for x, car in enumerate(self.cars):
        #     new_row = 0
        #     new_col = 0
        #     if car.horiz:
        #         new_col = 1
        #     else:
        #         new_row = 1

        #     i, j = car.row, car.col
        #     for k in range(car.length):
        #         print(k)
        #         grid[i][j] = car.letter
        #         i += new_row
        #         j += new_col
        puzzle = self.puzzle
        grid = [[0 for x in range(self.N)] for y in range(self.N)] 
        count=0
        # places puzzle in a 2x2 grid
        for i in range(self.N):
            for j in range(self.N):
                grid[i][j] = puzzle[count]
                count += 1
        return grid

    # Return list of possible states (moves) from current state
    def get_next_state(self):

        listOfMoves = []
        grid = self.get_state_grid()

        for x, car in enumerate(self.cars):
            row = car.row
            new_row = 0
            col = car.col
            new_col = 0

            # Move Down / Right
            if car.horiz:
                new_col = 1
                col += car.length
            else:
                new_row = 1
                row += car.length
            if row < self.N and col < self.N and grid[row][col] == '.':
                move = self.cloneState()
                move.cars[x].row += new_row
                move.cars[x].col += new_col
                listOfMoves.append(move)

            # Move Up / Left
            if car.horiz:
                new_col = 1
                col -= car.length
            else:
                new_row = 1
                row -= car.length
            if row < self.N and col < self.N and grid[row][col] == '.':
                move = self.cloneState()
                move.cars[x].row -= new_row
                move.cars[x].col -= new_col
                listOfMoves.append(move)

        return listOfMoves