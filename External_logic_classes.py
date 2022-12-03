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
        self.ask()
        self.opponent_board.shot()


class User(Player):
    def ask(self):
        while True:
            try:
                player_shot = int(input("В какую ячейку будем стрелять? "))
                row = player_shot // 10 - 1
                col = player_shot % 10 - 1
                return (row, col)

            except Exception:
                print('Необходимо ввести двузначное число, каждая цифра которого от 1 до 6! ')
                continue


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
        ship_types = [(3, 1), (2, 2), (1, 4)]  # формат - (длина корабля, количество кораблей)

        for i in ship_types:
            for j in range(i[1]):
                rand_front = self.user_board.player_shots_left[randint(0, len(self.user_board.player_shots_left))].show
                ship = Ship(i[0], rand_front, randint(1, 2), i[0])
                print(i[0], rand_front, randint(1, 2), i[0])
                ship.dots()
                self.user_board.add_ship(ship)

    #         create a board
    #         apply to user_board

    #         create a board
    #         AI_board

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