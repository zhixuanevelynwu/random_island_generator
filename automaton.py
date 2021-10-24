#! /usr/bin/env python3
''' Run map generating algorithms. '''
import random


class Automata:

    def __init__(self, row, col, island_rate=48, mountain_rate=42, desert_rate=45):
        self.row = row
        self.col = col
        self.map = [[0 for _ in range(col)] for _ in range(row)]
        self.island_rate = island_rate
        self.mountain_rate = mountain_rate
        self.mountain_created = False
        self.desert_rate = desert_rate
        self.desert_created = False
        for i in range(0, self.row):
            for j in range(0, self.col):
                r = random.randint(1, 100)
                if r <= self.island_rate:   # Approximately island_rate% of being island.
                    self.map[i][j] = 1
        self.mountain_map = [[0 for _ in range(col)] for _ in range(row)]
        self.desert_map = [[0 for _ in range(col)] for _ in range(row)]

    def printMap(self):
        for x in range(self.row):
            for y in range(self.col):
                print(self.map[x][y], end='  ')
            print("\n")
        print(" ")

    def mountain_simulation(self, generations, birthLimit, deathLimit):
        if not self.mountain_created:   # create  mountain if not created
            self.mountain_created = True
            for i in range(0, self.row):
                for j in range(0, self.col):
                    r = random.randint(1, 100)
                    # mountain_rate% of being mountain.
                    if r <= self.mountain_rate and self.map[i][j] == 1:
                        self.mountain_map[i][j] = 1
        else:
            ''' generations '''
            temp = [[0 for _ in range(self.col)] for _ in range(self.row)]
            for _ in range(generations):
                for x in range(self.row):
                    for y in range(self.col):
                        count = self.mountain_map_surroundings(x, y)
                        if self.map[x][y] != 0:  # only run when the grid is not ocean
                            isMountain = self.isMountain(
                                self.mountain_map[x][y], count, birthLimit, deathLimit)
                        else:
                            isMountain = 0
                        temp[x][y] = isMountain
                self.mountain_map = temp
            ''' end stage '''

    def isMountain(self, isAlive, count, birthLimit, deathLimit):
        if isAlive == 1:
            if count < deathLimit:
                return 0
            else:
                return 1
        else:
            if count > birthLimit:
                return 1
            else:
                return 0

    def mountain_map_surroundings(self, x, y):
        count = 0

        ''' edge cases '''
        if x < 1 or x == self.row - 1:
            offset_x = 1 if x < 1 else -1
            offset_y = 1 if y < 1 else -1

            count += self.mountain_map[x+offset_x][y]
            count += self.mountain_map[x][y+offset_y]
            count += self.mountain_map[x+offset_x][y+offset_y]

            if y < 1 or y == self.col - 1:
                ''' 3 neighbors '''
                return count
            else:
                ''' 5 neighbors '''
                count += self.mountain_map[x][y-offset_y]
                count += self.mountain_map[x+offset_x][y-offset_y]
                return count

        if y < 1 or y == self.col - 1:
            ''' 5 neighbors '''
            offset_y = 1 if y < 1 else -1
            count += self.mountain_map[x-1][y]
            count += self.mountain_map[x-1][y+offset_y]
            count += self.mountain_map[x+1][y]
            count += self.mountain_map[x+1][y+offset_y]
            count += self.mountain_map[x][y+offset_y]
            return count

        ''' general '''
        count += self.mountain_map[x+1][y]
        count += self.mountain_map[x+1][y+1]
        count += self.mountain_map[x+1][y-1]
        count += self.mountain_map[x][y+1]
        count += self.mountain_map[x][y-1]
        count += self.mountain_map[x-1][y]
        count += self.mountain_map[x-1][y-1]
        count += self.mountain_map[x-1][y+1]

        return count

    def desert_simulation(self, generations, birthLimit, deathLimit):
        if not self.desert_created:   # create  desert if not created
            self.desert_created = True
            for i in range(0, self.row):
                for j in range(0, self.col):
                    r = random.randint(1, 100)
                    rate = self.desert_rate
                    if self.surroundings(i, j) <= 7:
                        rate = rate * 2
                        # larger rate of being desert if near ocean
                    if r <= rate and self.map[i][j] == 1 and self.mountain_map[i][j] == 0:
                        # desert_rate% of being desert.
                        self.desert_map[i][j] = 1

        else:
            ''' generations '''
            temp = [[0 for _ in range(self.col)] for _ in range(self.row)]
            for _ in range(generations):
                for x in range(self.row):
                    for y in range(self.col):
                        count = self.desert_map_surroundings(x, y)
                        if self.map[x][y] != 0 and self.mountain_map[x][y] == 0:
                            # only run when the grid is not ocean and mountain
                            isDesert = self.isDesert(
                                self.desert_map[x][y], count, birthLimit, deathLimit)
                        else:
                            isDesert = 0
                        temp[x][y] = isDesert
                self.desert_map = temp
            ''' end stage '''

    def isDesert(self, isAlive, count, birthLimit, deathLimit):
        if isAlive == 1:
            if count < deathLimit:
                return 0
            else:
                return 1
        else:
            if count > birthLimit:
                return 1
            else:
                return 0

    def desert_map_surroundings(self, x, y):
        count = 0

        ''' edge cases '''
        if x < 1 or x == self.row - 1:
            offset_x = 1 if x < 1 else -1
            offset_y = 1 if y < 1 else -1

            count += self.desert_map[x+offset_x][y]
            count += self.desert_map[x][y+offset_y]
            count += self.desert_map[x+offset_x][y+offset_y]

            if y < 1 or y == self.col - 1:
                ''' 3 neighbors '''
                return count
            else:
                ''' 5 neighbors '''
                count += self.desert_map[x][y-offset_y]
                count += self.desert_map[x+offset_x][y-offset_y]
                return count

        if y < 1 or y == self.col - 1:
            ''' 5 neighbors '''
            offset_y = 1 if y < 1 else -1
            count += self.desert_map[x-1][y]
            count += self.desert_map[x-1][y+offset_y]
            count += self.desert_map[x+1][y]
            count += self.desert_map[x+1][y+offset_y]
            count += self.desert_map[x][y+offset_y]
            return count

        ''' general '''
        count += self.desert_map[x+1][y]
        count += self.desert_map[x+1][y+1]
        count += self.desert_map[x+1][y-1]
        count += self.desert_map[x][y+1]
        count += self.desert_map[x][y-1]
        count += self.desert_map[x-1][y]
        count += self.desert_map[x-1][y-1]
        count += self.desert_map[x-1][y+1]

        return count

    def life_stage(self, generations):
        ''' generations '''
        temp = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for _ in range(generations):
            for x in range(self.row):
                for y in range(self.col):
                    count = self.surroundings(x, y)
                    deadORalive = self.dead_or_alive(self.map[x][y], count)
                    temp[x][y] = deadORalive
            self.map = temp
        ''' end stage '''

    def island_simulation(self, generations, birthLimit, deathLimit):
        ''' generations '''
        temp = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for _ in range(generations):
            for x in range(self.row):
                for y in range(self.col):
                    count = self.surroundings(x, y)
                    isIsland = self.isIsland(
                        self.map[x][y], count, birthLimit, deathLimit)
                    temp[x][y] = isIsland
            self.map = temp
        ''' end stage '''

    def isIsland(self, isAlive, count, birthLimit, deathLimit):
        if isAlive == 1:
            if count < deathLimit:
                return 0
            else:
                return 1
        else:
            if count > birthLimit:
                return 1
            else:
                return 0

    def dead_or_alive(self, isAlive, count):
        '''
            If a living cell has less than two living neighbours, it dies.
            If a living cell has two or three living neighbours, it stays alive.
            If a living cell has more than three living neighbours, it dies.
            If a dead cell has exactly three living neighbours, it becomes alive.
        '''
        if count < 2:
            return 0
        if isAlive == 1:
            if count > 3:
                return 0
        elif isAlive == 0:
            if count == 3:
                return 1
        return isAlive

    def surroundings(self, x, y):
        count = 0

        ''' edge cases '''
        if x < 1 or x == self.row - 1:
            offset_x = 1 if x < 1 else -1
            offset_y = 1 if y < 1 else -1

            count += self.map[x+offset_x][y]
            count += self.map[x][y+offset_y]
            count += self.map[x+offset_x][y+offset_y]

            if y < 1 or y == self.col - 1:
                ''' 3 neighbors '''
                return count
            else:
                ''' 5 neighbors '''
                count += self.map[x][y-offset_y]
                count += self.map[x+offset_x][y-offset_y]
                return count

        if y < 1 or y == self.col - 1:
            ''' 5 neighbors '''
            offset_y = 1 if y < 1 else -1
            count += self.map[x-1][y]
            count += self.map[x-1][y+offset_y]
            count += self.map[x+1][y]
            count += self.map[x+1][y+offset_y]
            count += self.map[x][y+offset_y]
            return count

        ''' general '''
        count += self.map[x+1][y]
        count += self.map[x+1][y+1]
        count += self.map[x+1][y-1]
        count += self.map[x][y+1]
        count += self.map[x][y-1]
        count += self.map[x-1][y]
        count += self.map[x-1][y-1]
        count += self.map[x-1][y+1]

        return count


def main():
    pass


if __name__ == "__main__":
    main()
