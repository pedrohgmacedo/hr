n = int(input())

li = []
commands = {"insert": li.insert,
            "remove": li.remove,
            "append": li.append,
            "sort": li.sort,
            "pop": li.pop,
            "reverse": li.reverse}

args = []
for _ in range(n):
    command, *line = input().split()
    args = list(map(int, line))
    if command != "print":
        commands[command](*args)
    else:
        print(li)
