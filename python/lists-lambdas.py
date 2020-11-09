n = int(input())

commands = {"insert": lambda li, args: li.insert(*args),
            "remove": lambda li, args: li.remove(*args),
            "append": lambda li, args: li.append(*args),
            "sort": lambda li, args: li.sort(*args),
            "pop": lambda li, args: li.pop(*args),
            "reverse": lambda li, args: li.reverse(*args),
            "print": lambda li, args: print(li)
            }

li = []
args = []
for _ in range(n):
    command, *line = input().split()
    args = list(map(int, line))
    commands[command](li, args)
