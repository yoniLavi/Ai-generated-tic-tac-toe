import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Tic-Tac-Toe game with AI opponent")
    parser.add_argument("-d", "--difficulty", type=int, choices=[1, 2, 3], default=2,
                        help="Set AI difficulty level (1: Easy, 2: Medium, 3: Hard)")
    parser.add_argument("-p", "--player", type=str, choices=['X', 'O'], default='X',
                        help="Choose player symbol (X or O)")
    return parser.parse_args()
