from Internal_logic_classes import BoardOutError, NonEmptyError, ShipLocationError, Dot, Ship, Board
from External_logic_classes import Player, User, AI, Game

user_board = Board(hid = False)
AI_board = Board(hid = True)
user = User(user_board, AI_board)
ai = AI(AI_board, user_board)

g = Game(user, user_board, AI, AI_board)
g.random_board()