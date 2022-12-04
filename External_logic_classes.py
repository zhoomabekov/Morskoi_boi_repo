from Internal_logic_classes import BoardOutError, NonEmptyError, ShipLocationError, Dot, Ship, Board

from abc import ABC
from abc import abstractmethod
from random import randint


class Player(ABC):
    def __init__(self, my_board, opponent_board):
        self.my_board = my_board
        self.opponent_board = opponent_board
        super().__init__()

    @abstractmethod
    def ask(self):
        pass

    def move(self):
        self.opponent_board.shot(self.ask())


class User(Player):
    def ask(self):
        while True:
            try:
                player_shot = int(input("В какую ячейку будем стрелять? "))
                row = player_shot // 10 - 1
                col = player_shot % 10 - 1
                return row, col

            except Exception:
                print('Необходимо ввести двузначное число, каждая цифра которого от 1 до 6! ')
                continue

                # AI CLASS


class AI(Player):
    def ask(self):
        shot = self.opponent_board.player_shots_left[randint(0, len(self.opponent_board.player_shots_left) - 1)]
        return shot.show


class Game:
    def __init__(self, user, user_board, AI, AI_board):
        self.user = user
        self.user_board = user_board
        self.AI = AI
        self.AI_board = AI_board

    def random_board(self):
        hid = 0
        while True:
            temp = Board(hid)
            if hid > 1:
                break
            # размещение 3-клеточного корабля
            while True:
                try:
                    rand_front = temp.player_shots_left[
                        randint(0, len(temp.player_shots_left) - 1)].show
                    ship = Ship(3, rand_front, randint(1, 2), 3)

                    temp.add_ship(ship)
                    break
                except Exception:
                    print('exception when 3x user')
                    continue

            # размещение 2-клеточных кораблей
            trial = 10000
            n = 2
            while True:
                try:
                    rand_front = temp.player_shots_left[
                        randint(0, len(temp.player_shots_left) - 1)].show
                    ship = Ship(2, rand_front, randint(1, 2), 2)

                    temp.add_ship(ship)
                    n -= 1
                    if n == 0:
                        break
                    else:
                        continue

                except Exception:
                    if trial == 0:
                        break
                    else:
                        trial -= 1
                    continue

            if trial == 0:
                temp.ships = []
                print('start over after TWO user')
                continue

            # размещение 1-клеточных кораблей
            trial = 10000
            n = 4
            while True:
                try:
                    rand_front = temp.player_shots_left[
                        randint(0, len(temp.player_shots_left) - 1)].show
                    ship = Ship(1, rand_front, randint(1, 2), 1)

                    temp.add_ship(ship)
                    n -= 1
                    if n == 0:
                        break
                    else:
                        continue

                except Exception:
                    if trial == 0 or n == 0:
                        break
                    else:
                        trial -= 1
                    continue

            if trial == 0:
                print('the end reached user')
                trial == 10000
                temp.ships = []
                print('start over user')
                continue
            else:
                if hid == 0:
                    user_board = temp
                elif hid == 1:
                    AI_board = temp
                hid += 1
        # while True:
        #     # размещение 3-клеточного корабля
        #     while True:
        #         try:
        #             rand_front = self.AI_board.player_shots_left[
        #                 randint(0, len(self.AI_board.player_shots_left) - 1)].show
        #             ship = Ship(3, rand_front, randint(1, 2), 3)
        #
        #             self.AI_board.add_ship(ship)
        #             break
        #         except Exception:
        #             print('exception when 3x')
        #             continue
        #
        #     # размещение 2-клеточных кораблей
        #     trial = 10000
        #     n = 2
        #     while True:
        #         try:
        #             rand_front = self.AI_board.player_shots_left[
        #                 randint(0, len(self.AI_board.player_shots_left) - 1)].show
        #             ship = Ship(2, rand_front, randint(1, 2), 2)
        #
        #             self.AI_board.add_ship(ship)
        #             n -= 1
        #             if n == 0:
        #                 break
        #             else:
        #                 continue
        #
        #         except Exception:
        #             if trial == 0:
        #                 break
        #             else:
        #                 trial -= 1
        #             continue
        #
        #     if trial == 0:
        #         self.AI_board.ships = []
        #         print('start over after TWO')
        #         continue
        #
        #     # размещение 1-клеточных кораблей
        #     trial = 10000
        #     n = 4
        #     while True:
        #         try:
        #             rand_front = self.AI_board.player_shots_left[
        #                 randint(0, len(self.AI_board.player_shots_left) - 1)].show
        #             ship = Ship(1, rand_front, randint(1, 2), 1)
        #
        #             self.AI_board.add_ship(ship)
        #             n -= 1
        #             if n == 0:
        #                 break
        #             else:
        #                 continue
        #
        #         except Exception:
        #             if trial == 0 or n == 0:
        #                 break
        #             else:
        #                 trial -= 1
        #             continue
        #
        #     if trial == 0:
        #         print('the end reached')
        #         trial == 10000
        #         self.AI_board.ships = []
        #         print('start over')
        #         continue
        #     else:
        #         break

    def greet(self):
        print('''Приветствую Вас, друг мой!
Перед началом игры позвольте рассказать о ее правилах''')

    def loop(self):
        while True:
            self.user.move()
            if self.AI_board.alive_ships == 0:
                print('User wins!')
                break
            self.AI.move()
            if self.user_board.alive_ships == 0:
                print('AI wins!')
                break

    def start(self):
        self.greet()
        self.loop()
