import os
from coords import Coordinates

class Connect:
    def __init__(self, x_limit, y_limit, connect_limit):
        self.X_LIMIT = x_limit
        self.Y_LIMIT = y_limit
        self.CONNECT_LIMIT = connect_limit
        self.PLAYERS = ['X','O']

        self.coord = Coordinates(x_limit, y_limit)
        self.c4 = [[0 for i in range(x_limit)] for j in range(y_limit)]
        self.filled_columns = []

    def get_item(self, x, y):
        return self.c4[y][x]

    def set_item(self, x, y, val):
        self.c4[y][x] = val

    def add(self, x, val):

        for y in range(self.Y_LIMIT):
            if self.get_item(x,y) != 0: break
            previous_y = y

        self.set_item(x, previous_y, val)
        if previous_y == 0: self.filled_columns.append(x)

        return [x, previous_y]

    def check(self, x, y, value):
        def common_check(func: callable, func1: callable):
            coordinates_list = [[x, y]]

            for i in [func, func1]:
                tempx, tempy = x, y

                while True:
                    coords = i(tempx, tempy)
                    element = self.get_item(*coords) if coords is not None else None
                    if element is None or element != value:
                        break
                    else:
                        tempx, tempy = coords
                        coordinates_list.append(coords)

            return len(coordinates_list) >= self.CONNECT_LIMIT

        # Horizontal check
        if common_check(self.coord.left_coord, self.coord.right_coord): return True


        # Vertical check
        if common_check(self.coord.up_coord, self.coord.down_coord): return True


        # Diagonal checks
        if common_check(self.coord.top_left_coord, self.coord.bottom_right_coord): return True


        if common_check(self.coord.top_right_coord, self.coord.bottom_left_coord): return True

        return False

    def draw(self, val):
        os.system('cls' if os.name == 'nt' else 'clear')

        x_spacing = 0
        y_spacing = 1

        for i in range(self.X_LIMIT):
            if i not in self.filled_columns:
                print(i+1, ' '*y_spacing,end='')
            else:
                print(' ', ' ' * y_spacing, end='')

        print()
        print()

        for i in self.c4:
            for j in i:
                if j == 0: val = '_'
                elif j == 1: val = self.PLAYERS[0]
                elif j == 2: val = self.PLAYERS[1]
                print(val,' '*y_spacing,end='')
            print()
        print()

    def run(self):
        run = True

        while run:
            for i in range(2):
                self.draw(i)

                print(f'Player {i+1}\'s Turn! ({self.PLAYERS[i]})')

                while True:
                    a = input('Enter Column: ')
                    if not a.isdigit():
                        print('Enter Column Number!')

                    elif int(a)-1 not in self.filled_columns and int(a) > self.X_LIMIT:
                        print('Incorrect Column!')

                    elif int(a)-1 in self.filled_columns:
                        print('Columns is Full!')

                    else: break

                    print()

                insert_column = int(a)-1

                inserted_coords = self.add(insert_column, i+1)

                if self.check(inserted_coords[0], inserted_coords[1], i+1):
                    run = False

                    self.draw(i)
                    print(f'Player {i+1} ({self.PLAYERS[i]}) has won!')

                    break
