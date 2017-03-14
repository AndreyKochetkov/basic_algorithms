def foo(l):
    stack = []
    for i in l:
        if i == "]":
            try:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)
            except IndexError:
                return False
        if i == "}":
            try:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)
            except IndexError:
                return False
        if i == ")":
            try:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(i)
            except IndexError:
                return False
        if i == "(" or i == "{" or i == "[":
            stack.append(i)

    if len(stack) == 0:
        return True
    else:
        return False