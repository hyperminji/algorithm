while True:
    try:
        n = int(input())
        abs='1'
        while True:
            if int(abs) % n == 0:
                print(len(abs))
                break
            abs = abs+'1'
    except EOFError:
        break
