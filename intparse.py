def commands(cmd):
    if cmd == "undo":
        undo()
        return True

    return False


def parseint(message, min, max, cmds=True):
    while True:
        val = input(message)

        if cmds and commands(val):
            continue

        try:
            number = int(val)
        except ValueError:
            print("Please write a number [{};{}]".format(min, max))
            continue

        if number < min:
            print("Number too low, [{};{}]".format(min, max))
            continue

        if number > max:
            print("Number too high, [{};{}]".format(min, max))
            continue

        return number


def undo():
    print("Undo")