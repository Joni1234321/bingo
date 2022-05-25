from scripts.intparse import parseint


class Game:
    def play(self):
        # Read number
        number = parseint(self, "Drawn number: ", 1, 90)

        # Check if number can be drawn
        if self.drawn_numbers[number]:
            print("Already drawn")
            return

        # Draw number
        self.drawn_numbers[number] = True
        self.draw_history.append(number)

        for plate in self.plates:
            plate.update_board(number)

    def undo(self):
        if len(self.draw_history) == 0:
            print("No numbers drawn, so can't undo")
            return

        # Undo the number
        undo_this_number = self.draw_history.pop()
        self.drawn_numbers[undo_this_number] = False

        for plate in self.plates:
            plate.undo_number(undo_this_number)


    def __init__(self, plates):
        # drawn_numbers is a list where every number drawn is 1 if it is
        self.drawn_numbers = [False] * 91  # 0 - 90
        # draw_history is the order in which the numbers are drawn, this is used for the undo function
        self.draw_history = []
        self.plates = plates

    def print_draw_numbers(self):
        s = ""
        for i in range(9):
            s += "|"
            for j in range(10):
                val = i * 10 + j
                # Zero is just xx to indicate not a valid number
                if val == 0:
                    s += " XX |"
                    continue

                # If the number is drawn
                if self.drawn_numbers[val]:
                    if val < 10:
                        s += " "  # Compensate for single digit numbers
                    s += " " + str(val) + " |"
                else:
                    s += "    |"
            s += "\n"
        if self.drawn_numbers[90]:
            s += "| 90 |"
        else:
            s += "|    |"
        print(s)
