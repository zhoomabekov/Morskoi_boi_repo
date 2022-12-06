from Internal_logic_classes import BoardOutError, NonEmptyError, ShipLocationError, Dot, Ship, Board
from External_logic_classes import Player, User, AI, Game

user_board = Board(hid=False)
AI_board = Board(hid=True)
test_user = Board(hid=False)
test_AI = Board(hid=True)

user = User(user_board, AI_board)
AI = AI(test_AI, test_user)

g = Game(user, user_board, AI, AI_board)
g.random_board()
