def Pyramide(text):
    Position = 1

    while len(text) > Position:
        print(text[0:Position:])

        text = text[Position::]
        Position += 1

text = "abcdefghijklmnopqrstuvwxyz" * 10

Pyramide(text)