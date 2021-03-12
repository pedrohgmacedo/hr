# def minion_game_sucks(string):
#     comb = []
#     stuart = 0
#     kevin = 0
#     l = len(string)

#     # gets all combinations
#     comb = [string[i:j] for i in range(l) for j in range(i + 1, l + 1)]
#     print(comb)
#     # returns only combinations that are continuous
#     res = [el for el in comb if string.rfind(el) != -1]

#     for el in res:
#         if el[0] in ['A', 'E', 'I', 'O', 'U']:
#             kevin += 1
#         else:
#             stuart += 1

#     if stuart > kevin:
#         print('Stuart {}'.format(stuart))
#     elif kevin > stuart:
#         print('Kevin {}'.format(kevin))
#     else:
#         print('Draw')

# :(
def minion_game(s):
    vowels = 'AEIOU'

    kevin = 0
    stuart = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin += (len(s)-i)
        else:
            stuart += (len(s)-i)

    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
