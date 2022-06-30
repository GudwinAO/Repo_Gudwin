from sys import argv
try:
    script, pos, pos_last = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        x = 0
        for line in f:
            x += 1
            if int(pos) <= x <= int(pos_last):
                print(line)
except ValueError:
    try:
        script, pos = argv
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            x = 0
            for line in f:
                x += 1
                if int(pos) == x:
                    print(line)
    except ValueError:
        script = argv
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
