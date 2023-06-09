while 1:
    try:
        something = input()
        print(something)
    except EOFError:
        break