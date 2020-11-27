def mutate_string(string, position, character):
    s = list(string)
    s[position] = character
    return "".join(s)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# s = input()
# i, k = input().split()
# print(s[:int(i)]+k+s[int(i)+1:])
