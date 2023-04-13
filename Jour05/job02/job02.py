def draw_rectangle(width, height):

    print("+", end="")
    for i in range(width-2):
        print("-", end="")
    print("+")

    for j in range(height-2):
        print("|", end="")
        for i in range(width-2):
            print(" ", end="")
        print("|")

    print("+", end="")
    for i in range(width-2):
        print("-", end="")
    print("+")

draw_rectangle(25, 8)