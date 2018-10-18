import re


def exp_output(tree):
    out = list()
    if tree.type == 2:
        out.append('(')
        if tree.left:
            out += exp_output(tree.left)
        out.append('.')
        if tree.right:
            out += exp_output(tree.right)
        out.append(')')
    else:
        if tree.type == 0:
            out.append(str(tree.val))
        else:
            out.append(tree.name)
    return out


def dfs(tree):

    if tree.type == 2:
        if tree.left:
            dfs(tree.left)
        if tree.right:
            dfs(tree.right)
    else:
        if tree.type == 0:
            print(tree.val)
        else:
            print(tree.name)


def exp_strip(exp):
    return re.sub(' +', ' ', exp).strip()


def extract_parts(exp):
    parts = []          # check end-cases

    while len(exp)>0:
        ls = exp.find('(')
        if ls == -1:
            parts += exp.split()
            exp = ''
        elif ls == 0:
            r = get_the_bracket(ls,exp)
            parts.append(exp[ls:r + 1])
            exp = exp[r + 2:]
        else:
            parts += exp[:ls].split()
            exp = exp[ls:]

    return parts


class SExp:
    def __init__(self):
        self.type = None  # 0 = int, 2 = literal, 3 = non-atomic
        self.val = None
        self.name = None
        self.left = None
        self.right = None


# NIL atom
nil = SExp()
nil.type = 1
nil.name = 'NIL'


def get_the_bracket(i,exp):
    j = i
    c = 1
    while c!=0:
        j+=1
        if exp[j]=='(':
            c+=1
        elif exp[j]==')':
            c-=1

    return j


def check_bracket(exp):
    c = 0
    i = 0
    while(i<len(exp)):
        if exp[i]=='(':
            c+=1
        elif exp[i]==')':
            c-=1
        i+=1
    return c


def exp_input(x):
    full_x = []
    while 1:
        if x == '$':
            break
        else:
            full_x.append(x)
        x = input()
    full_x = ' '.join(full_x)

    # Check for errors
    if check_bracket(full_x) != 0:
        print('**error: missing parenthesis**')
        return None

    tree = make_tree(full_x)

    return tree


def make_tree(exp):
    tree = SExp()
    left_par = exp.find('(')
    right_par = exp.rfind(')')

    if left_par == -1 and right_par == -1:
        if re.match('[0-9]+',exp):
            exp = int(exp)
            tree.type = 0
            tree.val = exp
        else:  # Too general. No Restriction on literals
            if ' ' in exp:
                print('**error missing parenthesis**')
            elif '$' in exp:
                print('**error: unexpected $**')
                return None
            elif not  re.match('[A-Z]+[a-zA-Z0-9]*',exp):
                print('**error: wrong symbolic '+exp+'**')
                return None

            tree.type = 1
            tree.name = exp
    else:
        tree.type = 2
        exp = exp_strip(exp[left_par+1:right_par])
        parts = extract_parts(exp)
        if '.' in parts:
            if len(parts) == 3 and parts[1]=='.':
                tree.left = make_tree(parts[0])
                tree.right = make_tree(parts[2])
            else:
                print("**error: unexpected dot**")
                return None
        elif len(parts) > 0:
            temp = tree
            for i in parts[:-1]:
                temp.left = make_tree(i)
                temp.right = SExp()
                temp = temp.right
                temp.type = 2
            temp.left = make_tree(parts[-1])
            temp.right = nil
        else:
            tree.type = 1
            tree = nil

    return tree


if __name__ == '__main__':
    pass
