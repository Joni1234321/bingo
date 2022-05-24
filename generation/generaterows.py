import random

# how many columns
NUMBER_KEYS = range(9)
# how many rows
N_ROWS = range(3)


# Generate the rows for each plate
def generate_plate():
    # The columns
    columns = [[]] * len(NUMBER_KEYS)

    # Make dictionary
    for i in NUMBER_KEYS:
        columns[i] = []

    # Generate numbers
    generated = 0
    while generated < 15:
        n = random.randint(1, 90)
        column = int(n / 10)
        # edge case
        if n == 90:
            column = 8

        # Fail
        if len(columns[column]) == 3:
            continue
        if n in columns[column]:
            continue

        # Success
        columns[column].append(n)
        generated = generated + 1

    # Sort numbers
    for i in NUMBER_KEYS:
        columns[i] = sorted(columns[i])

    # Spread numbers
    rows = spread_numbers(columns)

    for i in N_ROWS:
        rows[i] = sorted(rows[i])

    # Check if valid
    if is_valid_plate(rows, columns):
        return rows

    return generate_plate()

def is_valid_plate (rows, columns):
    # check for empty columns
    empty_cols = 0
    for col in columns:
        if len(col) == 0:
            empty_cols += 1

    # Max two empty cols otherwise generate a new one
    if empty_cols > 1:
        return False

    return True

# Spread the numbers out on rows so there are 5 on each row
def spread_numbers(columns):
    # Numbers left to spread on each row
    left_per_row = [5] * 3
    rows = [[], [], []]

    # Spread the columns that have 3 numbers
    for c in NUMBER_KEYS:
        column = columns[c]
        if len(column) == 3:
            for row in range(3):
                rows[row].append(column[row])
                left_per_row[row] -= 1

    # Spread those that have 2
    for c in NUMBER_KEYS:
        column = columns[c]
        if len(column) == 2:
            # Get lowest row and place the numbers in the two other rows
            lowest = 0
            if left_per_row[1] < left_per_row[lowest]:
                lowest = 1

            if left_per_row[2] < left_per_row[lowest]:
                lowest = 2

            highest = list(range(3))
            highest.remove(lowest)

            # Insert numbers into the two rows that have the highest value
            for i in range(2):
                row = highest[i]
                rows[row].append(column[i])
                left_per_row[row] -= 1

    # Check for rows that are not full
    unfilled_rows = list(range(3))
    for i in unfilled_rows:
        if left_per_row[i] == 0:
            unfilled_rows.remove(i)

    # Spread the rest
    for c in NUMBER_KEYS:
        column = columns[c]

        if len(column) == 1:
            # Insert number into random not full row
            insert_at = random.choice(unfilled_rows)
            rows[insert_at].append(column[0])

            # Reduce and remove if row is full
            left_per_row[insert_at] -= 1
            if left_per_row[insert_at] == 0:
                unfilled_rows.remove(insert_at)

    return rows

