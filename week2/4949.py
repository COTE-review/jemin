while True:
    txt = input()
    if txt == ".":
        break
    txt = list(txt)
    test = []

    for i in range(len(txt)):
        if txt[i] == '(' or txt[i] == '[':
            test.append(txt[i])
        elif txt[i] == ')':
            if len(test) != 0 and test[-1] == '(':
                test.pop()
            else:
                test.append(')')
                break
        elif txt[i] == ']':
            if len(test) != 0 and test[-1] == '[':
                test.pop()
            else:
                test.append(']')
                break
    if len(test) != 0:
        print('no')
    else:
        print('yes')