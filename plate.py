import random
import copy


class Plate:
    # list of columns
    numbers_keys = range(10)
    n_rows = range(3)

    # THis is not ordenstal, just dont know what to call it, u give it the number of rows completed and it return the resut
    def ordenstal(self, n):
        if n == 1:
            return "one row"
        elif n == 2:
            return "two rows"
        elif n == 3:
            return "full board"
        return ""

    # Make sure that number is not already called otherwise you can get the same row twice
    def update_board(self, number):
        for r in self.n_rows:
            if number in self.rows_undrawn[r]:
                # On number got
                self.rows_undrawn[r].remove(number)
                if len(self.rows_undrawn[r]) == 0:
                    self.rows_completed += 1

                    print("Completed " + self.ordenstal(self.rows_completed) + " @ row " + str(
                        r + 1) + " on board: \n" + str(self))
                break  # No need to check further

    def undo_number(self, number):
        for r in self.n_rows:
            if number in self.rows[r]:
                self.rows_undrawn[r].append(number)
                if len(self.rows_undrawn[r]) == 1:
                    self.rows_completed -= 1
                    print("Reverted " + self.ordenstal(self.rows_completed) + " @ row " + str(
                        r + 1) + " on board: \n" + str(self))

    # Reset
    def reset(self):
        self.rows_undrawn = copy.deepcopy(self.rows)

    def __init__(self, rows):
        # The numbers in each row
        self.rows = rows
        # The numbers left in each row that has not been drawn
        self.rows_undrawn = copy.deepcopy(rows)
        # Keeping count on rows completed
        self.rows_completed = 0

    # Draw the plate
    def __str__(self):
        out = ""
        for row in self.rows:
            out += "| "
            i = 0
            for c in range(10):
                # Out of index
                if i == len(row) or int(row[i] / 10) != c:
                    out += "  "
                # Print number
                else:
                    if c == 0:
                        out += " "
                    out += str(row[i])
                    i += 1
                out += " | "
            out += "\n"
        return out
