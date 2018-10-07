import re

def exp_output(tree):
    out = list()
    if tree.type == 2:
        out.append('(')
        if tree.left:
            out+=exp_output(tree.left)
        out.append('.')
        if tree.right:
            out+=exp_output(tree.right)
        out.append(')')
    else:
        if tree.type == 0:
            out.append(str(tree.val))
        else:
            out.append(tree.name)
    return out


def exp_strip(exp):
    return re.sub(' +', ' ', exp).strip()


def extract_parts(exp):
    parts = []              #check end-cases

    while len(exp)>0:
        l = exp.find('(')
        if l == -1:
            return exp.split()
        elif l == 0:
            r = exp.find(')')
            parts.append(exp[l:r+1])
            exp = exp[r+2:]
        else:
            parts+= exp[:l].split()
            exp = exp[l:]

    return parts


class SExp:
    type = None # 0 = int, 2 = literal, 3 = non-atomic
    val = None
    name = None
    left = None
    right = None



# NIL atom
nil = SExp()
nil.type = 1
nil.name = 'NIL'


def compute_SExp(x):
    full_x = []
    while 1:
        if x =='$':
            break
        else:
            full_x.append(x)
        x = input()
    full_x = ' '.join(full_x)
    tree = make_tree(full_x)

    return tree


def make_tree(exp):
    tree = SExp()
    left_par = exp.find('(')
    right_par = exp.rfind(')')

    if left_par == -1 and right_par == -1:
        try:
            exp = int(exp)
            tree.type = 0
            tree.val = exp
        except:   # Too general. No Restriction on literals
            tree.type = 1
            tree.name = exp
    else:
        tree.type = 2
        exp = exp_strip(exp[left_par+1:right_par])
        parts = extract_parts(exp)
        if len(parts) == 3 and parts[1] == '.':
            tree.left = make_tree(parts[0])
            tree.right = make_tree(parts[2])
        elif len(parts)>0:
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

    None