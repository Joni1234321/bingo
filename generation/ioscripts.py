# USED FOR READ AND WRITE DATA

SEPERATOR_NAME = ":"

SEPERATOR_NUMBER = ","
SEPERATOR_ROW = ";"
SEPERATOR_PLATE = "|"
SEPERATOR_PLAYER = "\n"

# Converts a string to list
def data_to_plate(plate_data):
    plate = []
    rows = list(plate_data.split(SEPERATOR_ROW))
    for row in rows:
        #print(row)
        plate.append([int(n) for n in list(row.split(SEPERATOR_NUMBER))])
    return plate


# Convert rows to data string
def plate_to_data(rows):
    rows_string = []
    for row in rows:
        rows_string.append(SEPERATOR_NUMBER.join([str(n) for n in row]))
    return SEPERATOR_ROW.join(rows_string)


# Delete all content in file
def clear_file(file_name):
    f = open(file_name, "w")
    f.write("")
    f.close()


# Save settings to file given the name and plate
def save_plates(file_name, name, plates):
    f = open(file_name, "a")
    f.write(name + SEPERATOR_NAME)
    for plate in plates:
        f.write(plate_to_data(plate) + SEPERATOR_PLATE)

    f.write(SEPERATOR_PLAYER)
    f.close()


# Returns all settings and their corresponding from file given the right syntax
#
def read_names(file_name):
    names = {}
    f = open(file_name, "r")
    plates_data = f.read()
    f.close()

    # Foreach player
    for name_data in plates_data.split(SEPERATOR_PLAYER):
        if name_data == "":
            continue

        # Get name and settings
        (name, plates_data) = name_data.split(SEPERATOR_NAME)
        plates = []
        for plate_data in list(plates_data.split(SEPERATOR_PLATE)):
            if plate_data == "":
                continue
            plates.append(data_to_plate(plate_data))

        # Plates at name in dictionary
        names[name] = plates

    return names

