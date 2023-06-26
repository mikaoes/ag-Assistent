def print_board(state):
    board = f" {state.get(0, '1')} | {state.get(1, '2')} | {state.get(2, '3')} \n"
    board += "---|---|---\n"
    board += f" {state.get(3, '4')} | {state.get(4, '5')} | {state.get(5, '6')} \n"
    board += "---|---|---\n"
    board += f" {state.get(6, '7')} | {state.get(7, '8')} | {state.get(8, '9')} \n"
    return board


class TicTacToe:
    def __init__(self):
        self.running = True
        self.name = "TicTacToe"
        self.state = {}
        self.last_player = "o"
        self.is_first_round = True
        self.winner = None

    def __call__(self, args_list):
        self.running = True
        return self.play(args_list)

    def play(self, args_list):
        result = ""

        if self.is_first_round:
            result += "Willkommen bei Tic-Tac-Toe!\n"
            result += "Der Spieler 'x' beginnt. Bitte gib für jeden Zug die Zahl an," \
                      " die dem Feld entspricht, auf das du setzen möchtest.\n"
            self.is_first_round = False
            result += print_board(self.state)
            return result

        if len(args_list) != 1 or not args_list[0].isdigit():
            result += "Bitte das Feld für den nächsten Zug mit einer Zahl zwischen 1 und 9 angeben.\n"
            result += print_board(self.state)
            return result

        if self.state.get(int(args_list[0]) - 1) is not None:
            result += "Dieses Feld ist bereits belegt. Bitte ein anderes wählen.\n"
            result += print_board(self.state)
        else:
            self.state[int(args_list[0]) - 1] = self.next_player

            if winner := self.determine_winner():
                return self.end_game(winner)

            result += print_board(self.state)
            self.last_player = self.next_player
            result += f"\nDer Spieler '{self.next_player}' ist nun am Zug.\n"

        return result

    def end_game(self, winner):
        result = ""
        result += print_board(self.state)
        if winner != "b":
            result += f"\nDer Spieler '{winner}' hat gewonnen! Vielen Dank fürs Spielen!\n"
        else:
            result += f"\nUnentschieden! Vielen Dank fürs Spielen!\n"
        print(result)

        self.running = False
        self.state = {}
        self.last_player = "o"
        self.is_first_round = True

    def determine_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]

        for combination in winning_combinations:
            if self.state.get(combination[0]) == self.state.get(combination[1]) == self.state.get(combination[2]):
                return self.state.get(combination[0])

        if len(self.state) == 9:
            return "b"

        return None

    @property
    def next_player(self):
        return 'x' if self.last_player == 'o' else 'o'


game = TicTacToe()

commands = {
    "tictactoe": game,
    "tic-tac-toe": game,
    "stop": game.end_game,
}
