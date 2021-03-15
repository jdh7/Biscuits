import numpy as np

"""
(1) custom "biscuits" die, (1 ) D8, (1) D10, (1) D12, and (11) D6 - various colors and sizes

"""


class Die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        return np.random.randint(low=1, high=self.sides + 1, dtype=int)


class Biscuits(Die):
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.board = self.new_game()

    def roll(self):
        for i in self.board:
            if i[2] == "Picked up":
                pass
            else:
                i[2] = i[0].roll_die()
        return self.board

    def pick_up(self, dice):
        for i in dice:
            for j in self.board:
                if j[1] == i:
                    self.score += int(j[0].sides) - int(j[2])
                    j[2] = "Picked up"

        self.game_over = True
        for i in self.board:
            if not i[2] == "Picked up":
                self.game_over = False
                break

    def new_game(self):
        self.create_dice()
        self.board = [
            [self.d12, "d12", 1, ":        "],
            [self.d10, "d10", 1, ":        "],
            [self.d8, "d8", 1, ":         "],
            [self.biscuits, "biscuit", 1, ":    "],
            [self.d61, "1d6", 1, ":        "],
            [self.d62, "2d6", 1, ":        "],
            [self.d63, "3d6", 1, ":        "],
            [self.d64, "4d6", 1, ":        "],
            [self.d65, "5d6", 1, ":        "],
            [self.d66, "6d6", 1, ":        "],
            [self.d67, "7d6", 1, ":        "],
            [self.d68, "8d6", 1, ":        "],
            [self.d69, "9d6", 1, ":        "],
            [self.d610, "10d6", 1, ":       "],
            [self.d611, "11d6", 1, ":       "],
        ]
        return self.board

    def draw_board(self):
        for i in self.board:
            if i[2] == "Picked up":
                print(i[1], i[3], i[2])
            elif i[0].sides - i[2] == 0:
                print(i[1], i[3], i[2], "!!!")
            elif i[0].sides - i[2] == 1:
                print(i[1], i[3], i[2], "!")
            else:
                print(i[1], i[3], i[2])

    def create_dice(self):
        self.biscuits = Die(6)
        self.d61 = Die(6)
        self.d62 = Die(6)
        self.d63 = Die(6)
        self.d64 = Die(6)
        self.d65 = Die(6)
        self.d66 = Die(6)
        self.d67 = Die(6)
        self.d68 = Die(6)
        self.d69 = Die(6)
        self.d610 = Die(6)
        self.d611 = Die(6)
        self.d8 = Die(8)
        self.d10 = Die(10)
        self.d12 = Die(12)
