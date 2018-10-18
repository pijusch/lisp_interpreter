from Utilities import *


if __name__ == '__main__':
    x = None

    while 1:
        x = input()
        if x == '$$':
            break
        else:
            exp = exp_input(x)  # Use this for eval()
            if exp:
                print(' '.join(exp_output(exp)))
