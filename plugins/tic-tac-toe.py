class TicTacToe:
    def __init__(self):
        self.running = True
        self.name = "TicTacToe"
        self.state = {}

    def __call__(self, args_list):
        return self.play()

    def play(self):
        return self.print_board(self.state)

    def end_game(self):
        self.running = False

    def print_board(self, state):
        board = f" {state.get('0', ' ')} | {state.get('1', ' ')} | {state.get('2', ' ')} \n"
        board += "-----------\n"
        board += f" {state.get('3', ' ')} | {state.get('4', ' ')} | {state.get('5', ' ')} \n"
        board += "-----------\n"
        board += f" {state.get('6', ' ')} | {state.get('7', ' ')} | {state.get('8', ' ')} \n"
        return board


game = TicTacToe()

commands = {
    "tictactoe": game,
    "tic-tac-toe": game,
    "stop": game.end_game,
}