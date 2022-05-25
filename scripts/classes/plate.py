import random
import copy


class Plate:
    # list of columns
    n_columns = range(9)
    n_rows = range(3)

    # THis is not ordenstal, just dont know what to call it, u give it the number of rows completed and it return the resut
    def ordenstal(self, n):
        if n == 0:
            return "zero rows"
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

                    print(self.name + " has " + self.ordenstal(self.rows_completed) + " @ row " + str(
                        r + 1) + " on board: \n" + str(self))
                break  # No need to check further

    # Undo the number .>)
    def undo_number(self, number):
        for r in self.n_rows:
            if number in self.rows[r]:
                self.rows_undrawn[r].append(number)
                if len(self.rows_undrawn[r]) == 1:
                    self.rows_completed -= 1
                    print(self.name + " reverted to " + self.ordenstal(self.rows_completed) + " @ row " + str(
                        r + 1) + " on board: \n" + str(self))

    # Reset
    def reset(self):
        self.rows_undrawn = copy.deepcopy(self.rows)

    def __init__(self, name, rows):
        # The name of the owner of the row
        self.name = name
        # The numbers in each row
        self.rows = rows
        # The numbers left in each row that has not been drawn
        self.rows_undrawn = copy.deepcopy(rows)
        # Keeping count on rows completed
        self.rows_completed = 0

    def create_draw_array(self):
        # array, do this because "*" creates pointers
        out = [[0] * len(self.n_columns) for _ in self.n_rows]

        # for every row
        for r in self.n_rows:
            row = self.rows[r]
            idx = 0

            # for every column
            for c in self.n_columns:
                number = row[idx]

                # If the current inspected number is in column
                if int(number / 10) == c or (number == 90 and c == 8):
                    out[r][c] = number

                    # Go to next number
                    idx += 1
                    # Go to next row if gone through all numbers here
                    if idx == len(row):
                        break

        return out

    # Draw the plate
    def __str__(self):
        draw_array = self.create_draw_array()

        out = ""
        for r in draw_array:
            out += "| "
            for n in r:
                # Draw number
                if n != 0:
                    if n < 10:
                        out += " "
                    out += str(n)
                # Draw empty
                else:
                    out += "  "

                # Draw end
                out += " | "
            out += "\n"

        return out
