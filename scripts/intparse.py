# regex (|.*?)(\d+) -> $2\n

def commands(game, cmd):
    if cmd == "undo":
        game.undo()
        game.print_draw_numbers()
        return True

    # Easter egg
    if cmd == "Vendelbo" or cmd == "Jonas" or cmd == "currywurst" or cmd == "curryotto":
        print("CURRYWURST!!!")
        return True

    return False


# YES THIS IS SHIT CODE; BUT IT WORKS
def parseint(game, message, min, max, cmds=True):
    while True:
        val = input(message)

        if cmds and commands(game, val):
            continue

        try:
            number = int(val)
        except ValueError:
            print("Please write a number [{};{}]".format(min, max))
            continue

        if number < min:
            print("Number too low [{};{}]".format(min, max))
            continue

        if number > max:
            print("Number too high [{};{}]".format(min, max))
            continue

        return number
