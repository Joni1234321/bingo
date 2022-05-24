from generation.generaterows import generate_plate
from generation.ioscripts import clear_file, save_plates
from plate import Plate
import sys

DATA_FILE = "plates/data"
NAME_FILE = "plates/names.txt"


def generate(n):
    names = read_names(NAME_FILE)
    print("Generating {} plates for {} names".format(n, len(names)))

    clear_file(DATA_FILE)
    for name in names:
        print(name)
        plates = []
        for i in range(n):
            plate = generate_plate()
            plates.append(plate)

            # Print
            print(Plate(plate))

        save_plates(DATA_FILE, name, plates)
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


n_plates = 3
if len(sys.argv) == 2:  #
    try:
        generate(int(sys.argv[1]))
    except:
        print("Error: no integer")
elif len(sys.argv) == 3:  # Names and generations
    pass
