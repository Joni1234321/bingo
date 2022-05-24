# Press Shift+F10 to execute it or replace it with your code.
from plate import Plate
from generation.drawplate import draw_plate
from game import Game
from generation.ioscripts import read_names

FILE_NAME = "plates/data"

plates = []


def start():
    plate_names = read_names(FILE_NAME)

    for p in plate_names:
        for rows in p:
            p = Plate(rows)
            plates.append(p)
            print(p)

    draw_plate(plates[0])

    game = Game(plates)

    while True:
        game.play()
        game.print_draw_numbers()

    # Check if valid


if __name__ == '__main__':
    start()
