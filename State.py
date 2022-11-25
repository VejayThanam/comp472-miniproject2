import Car

# Define State class (state of the game board)
class State:
    def __init__(self, line):
        self.N = 6  # size of board
        self.cars = []  # num of cars
        self.goal = 4  # end goal
        self.prev = None  # previous state
        self.puzzle = line

    # Makes copy of current state of the board
    def cloneState(self):
        s = State(self.puzzle)
        s.N = self.N
        for c in self.cars:
            s.cars.append(Car.Car(c.row, c.col, c.length, c.horiz, c.letter, c.fuel))
        s.goal = self.goal
        s.puzzle = self.puzzle
        return s

    # Load puzzle using file
    def load_puzzle(self):
        count = 0
        grid = [[0 for x in range(self.N)] for y in range(self.N)] 

        # places puzzle in a 2-D grid 6x6
        for i in range(self.N):
            for j in range(self.N):
                grid[i][j] = self.puzzle[count]
                count += 1
        
        # retrieves length of each car in puzzle and initializes each car with default 100 fuel
        puzzle=''.join(self.puzzle)          
        length = {}
        carFuel = {}
        for i in puzzle: 
            if i != '.':
                if i in length: 
                    length[i]=length[i] + 1
                else: 
                    length[i] = 1
                if i not in carFuel.keys():
                    carFuel[i]=100

        # assign specific car with given fuel parameters
        fuel = []
        # splits input string into separate components depending on if fuel is given
        word = self.puzzle.split()
        #checks if input string(game) has fuel given and stores fuel in new array
        if len(word) > 1:
            fuel += word[1:]
         # loops through fuel array and assigns new fuel to given cars
            if len(fuel) > 0:
                for i in range(len(fuel)):
                    carLetter = fuel[i]
                    if carLetter[0] in carFuel.keys():
                        carFuel[carLetter[0]] = int(carLetter[1])

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
       
        # stores car into state.cars list
        for car in carList:
            self.cars.append(Car.Car(carList[car][0], carList[car][1], carList[car][2], carList[car][3], car, carFuel[car]))

    # Return state of board as String
    def get_state_string(self):
        s = ""
        grid = self.get_state_grid()
        str = sum(grid, [])
        s = ''.join(str)
        return s

    # Returns NxN 2-D Matrix of State
    def get_state_grid(self):
        grid = [['.']*self.N for i in range(self.N)]
        for car in self.cars:
            for i in range(self.N):
                for j in range(self.N):
                    if car.row==i and car.col==j:
                        grid[i][j]=car.letter
                        if car.horiz and car.length==2:           
                                grid[i][j+1]=car.letter
                        elif car.horiz:
                                grid[i][j+1]=car.letter
                                grid[i][j+2]=car.letter
                        elif not car.horiz and car.length==2:
                            grid[i+1][j]=car.letter
                        elif not car.horiz:
                            grid[i+1][j]=car.letter
                            grid[i+2][j]=car.letter
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
            if row < self.N and col < self.N and grid[row][col] == '.' and car.fuel > 0:
                move = self.cloneState()
                move.cars[x].row += new_row
                move.cars[x].col += new_col
                move.cars[x].fuel -= 1
                listOfMoves.append(move)
                continue

            row = car.row
            new_row = 0
            col = car.col
            new_col = 0

            # Move Up / Left
            if car.horiz:
                new_col = 1
                col -= 1
            else:
                new_row = 1
                row -= 1
            if row >= 0 and col >= 0 and grid[row][col] == '.' and car.fuel > 0:
                move = self.cloneState()
                move.cars[x].row -= new_row
                move.cars[x].col -= new_col
                move.cars[x].fuel -= 1
                listOfMoves.append(move)
                continue

        return listOfMoves

    def get_red_car(self):
        for car in self.cars:
            if car.letter == 'A':
                return car