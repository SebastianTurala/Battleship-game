import random

matrix2 = [['','','','','','','','','',''],
          ['','','','','','','','','',''],
          ['','','','','','','','','',''],
          ['','','','','','','','','',''],
          ['','','','','','','','','',''],
          ['','','','','','','','','',''],
          ['','','','','','','','','',''],
          ['','','','','','','','','',''],
          ['','','','','','','','','',''],
          ['','','','','','','','','','']]

class Ship:
    def __init__(self, hp, symbol):
        self.hp = hp
        self.symbol = symbol
        self. symbols_list = ['A', 'B', 'C', 'F']

    def direct(self):
        direction_list = ['x','y']
        return random.choice(direction_list)

    def check_position(self, HP, dir, row, col):
        global matrix2

        if dir == 'x':
            for i in range(HP + 2):
                if row - 1 < 0 or col + 1 > 11 or col-1 < 0:
                    pass
                else:
                    if matrix2[row - 1][col - 1] in self.symbols_list:
                        return False

                if col - 1 < 0 or col + 1 > 11:
                    pass
                else:
                    if matrix2[row][col - 1] in self.symbols_list:
                        return False


                if row + 1 > 9 or col + 1 > 11 or col-1 < 0:
                    pass
                else:
                    if matrix2[row + 1][col - 1] in self.symbols_list:
                        return False

                col += 1
            return True

        if dir == 'y':
            for i in range(HP + 2):
                if col - 1 < 0 or row + 1 > 11 or row -1 < 0:
                    pass
                else:
                    if matrix2[row-1][col-1] in self.symbols_list:
                        return False

                if row - 1 < 0 or row + 1 > 11:
                    pass
                else:
                    if matrix2[row-1][col] in self.symbols_list:
                        return False

                if row + 1 > 11 or row - 1 < 0 or col + 1 > 9:
                    pass
                else:
                    if matrix2[row-1][col+1] in self.symbols_list:
                        return False
                row += 1
            return True

    def place_ship(self):
        hp = self.hp
        while True:
            dir = self.direct()
            if dir == 'x':
                row = random.randint(0, 9)
                col = random.randint(0, 10 - hp)
            if dir == 'y':
                row = random.randint(0,10 - hp)
                col = random.randint(0,9)

            if self.check_position(hp,dir,row,col) == True:
                if dir == 'x':
                    for i in range(self.hp):
                        matrix2[row][col] = self.symbol
                        col +=1
                if dir == 'y':
                    for i in range(self.hp):
                        matrix2[row][col] = self.symbol
                        row +=1
                break



def random_playboard():
    global matrix2
    aircraft = Ship(5, 'A')
    battleship1 = Ship(4, 'B')
    battleship2 = Ship(4, 'B')
    cruiser1 = Ship(3, 'C')
    cruiser2 = Ship(3, 'C')
    cruiser3 = Ship(3, 'C')
    fregate1 = Ship(2, 'F')
    fregate2 = Ship(2, 'F')
    aircraft.place_ship()
    battleship1.place_ship()
    battleship2.place_ship()
    cruiser1.place_ship()
    cruiser2.place_ship()
    cruiser3.place_ship()
    fregate1.place_ship()
    fregate2.place_ship()
    return matrix2