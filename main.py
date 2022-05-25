# Press Shift+F10 to execute it or replace it with your code.
from scripts.classes.plate import Plate
from scripts.classes.game import Game
from scripts.generation.ioscripts import read_names

FILE_NAME = "scripts/generation/data"

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
