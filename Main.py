from Utilities import *


def dfs(tree):

    if tree.type == 2:
        if tree.left:
            dfs(tree.left)
        if tree.right:
            dfs(tree.right)
    else:
        if tree.type ==0:
            print(tree.val)
        else:
            print(tree.name)


if __name__ == '__main__':
    x = None

    while 1:
        x = input()
        if x == '$$':
            break
        else:
            exp = compute_SExp(x) # Use this for eval()
            #dfs(exp)
            print(' '.join(exp_output(exp)))