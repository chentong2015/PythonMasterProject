def test_while():
    running = True
    while running:
        guess = int(input('Enter a number:'))
        if guess == 20:
            running = False
        elif guess > 30:
            print("too large")
        else:
            print("it's wrong")


def test_for_in():
    for index in range(1, 20):
        print("i=", index)


def test_break_continue():
    for index in range(20, 100):
        if index == 30:
            break
        else:
            print(index)
            continue


