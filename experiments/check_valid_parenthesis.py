from data_structure import Stack

def check_valid_bracket(value):
    stack = Stack()
    open_brac = ['(', '[', '{']
    for curr_brac in value:
        if curr_brac not in ['(', '[', '{', '}', ']', ')']:
            continue
        if curr_brac in open_brac:
            stack.push(curr_brac)
        else:
            if len(stack) == 0:
                return False
            poped_brac = stack.pop()
            if poped_brac == '(':
                if curr_brac != ')': return False
            if poped_brac == '[':
                if curr_brac != ']': return False
            if poped_brac == '{':
                if curr_brac != '}': return False

    if len(stack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    str_ = "({a+b})"
    print(check_valid_bracket(str_))
