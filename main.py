# Press Shift+F10 to execute it or replace it with your code.
from plate import Plate
from game import Game
from generation.ioscripts import read_names

FILE_NAME = "generation/data"

plates = []


def start():
    # Generate settings
    plate_names = read_names(FILE_NAME)

    for player in plate_names.items():
        (name, player_plates) = player
        print(name)
        for rows in player_plates:
            p = Plate(name, rows)
            plates.append(p)
            print(p)

    game = Game(plates)

    # Play
    while True:
        game.play()
        game.print_draw_numbers()

    # Check if valid


if __name__ == '__main__':
    start()
