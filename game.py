from intparse import parseint


class Game:
    def play(self):
        # TODO: Implement undo
        number = parseint("Drawn number: ", 1, 99)

        if self.drawn_numbers[number - 1] == 1:
            print("Already drawn")
            return

        self.drawn_numbers[number - 1] = 1

        for plate in self.plates:
            plate.update_board(number)

    def __init__(self, plates):
        self.drawn_numbers = [0] * 99  # 1 - 99
        self.plates = plates

    def print_draw_numbers(self):
        s = ""
        for i in range(10):
            s += "|"
            for j in range(10):
                val = i * 10 + j
                # Zero is just xx to indicate not a valid number
                if val == 0:
                    s += " XX |"
                    continue

                if self.drawn_numbers[val - 1] == 1:
                    if val < 10:
                        s += " "  # Compensate for single digit numbers
                    s += " " + str(val) + " |"
                else:
                    s += "    |"
            s += "\n"
        print(s)
