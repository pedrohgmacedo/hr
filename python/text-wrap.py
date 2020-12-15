def wrap(string, max_width):
    n = int(len(string)/max_width)+1

    wrapped_text = str()
    for i in range(n):
        paragraph = slice(i*max_width, (i+1)*max_width)
        wrapped_text += string[paragraph] + "\n"
    return wrapped_text


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
