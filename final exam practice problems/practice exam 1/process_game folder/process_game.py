def process_game(filename, handler) :
    with open(filename, 'r') as file: 
        game_state = file.read().strip()
        handler(game_state)

def print_game(game_state) :
    for i in range(0, 81, 9) :
        print(''.join(game_state[i:i+9]))

if __name__ == "__main__":
# Assume the file 'game.txt' contains a valid Sudoku game state
    process_game('game.txt', print_game)