from generation.generaterows import generate_plate
from generation.ioscripts import clear_file, save_plates
from generation.drawplate import player_to_pdf
from plate import Plate
import sys

DATA_FILE = "generation/data"
NAME_FILE = "settings/names.txt"


def generate(n):
    names = read_names(NAME_FILE)
    print("Generating {} settings each for {} names".format(n, len(names)))

    clear_file(DATA_FILE)
    for name in names:
        print(name)

        # Generate rows
        plates_rows = []
        for i in range(n):
            rows = generate_plate()
            plates_rows.append(rows)
        save_plates(DATA_FILE, name, plates_rows)

        # Generate PDF
        plates = []
        for rows in plates_rows:
            plate = Plate(name, rows)
            plates.append(plate)
            print(plate)

        player_to_pdf(plates)

    print("Generation complete!")
    print("Ida er fucking sej")
    print("OK MOTHERFUCKER")


# Returns a list of names
def read_names(file_name):
    names = []
    f = open(file_name, "r")
    names_data = f.read().split("\n")
    f.close()

    for name in names_data:
        if name == "":
            continue
        names.append(name)

    return names

if len(sys.argv) == 2:  #
    generate(int(sys.argv[1]))
elif len(sys.argv) == 3:  # Names and generations
    pass
