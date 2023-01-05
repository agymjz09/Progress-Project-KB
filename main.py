from easyAI import TwoPlayerGame, AI_Player, Negamax
from easyAI.Player import Human_Player

class TicTacToe_game(TwoPlayerGame):

    def __init__(self, players):
        self.players = players
        self.current_player = 1
        self.board = [0] * 9
    def possible_moves(self):
        return [x + 1 for x,y in enumerate(self.board) if y == 0]
    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player
    def umake_move(self, move):
        self.board[int(move) - 1] = 0
    def condition_for_lose(self):
        possible_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

        return any([all([(self.board[z - 1] == self.opponent) for z in combination]) for combination in possible_combinations])
    def is_over(self):
        return (self.possible_moves() == []) or self.condition_for_lose()
    def show(self):
        print('\n' + '\n'.join([' '.join([['.', '0', 'x'][self.board[3 * j + i]]
                               for i in range(3)]) for j in range(3)]))
    def scoring(self):
        return -100 if self.condition_for_lose() else 0
if __name__ == "__main__":
    algo = Negamax(7)

    TicTacToe_game([Human_Player(), AI_Player(algo)]).play()