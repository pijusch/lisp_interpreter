from Lisp import Lisp


if __name__ == '__main__':
    lisp = Lisp()

    while 1:
        x = input()
        if x == '$$':
            print('> bye!!')
            break
        else:
            exp = lisp.input(x)
            # eval()
            if exp:
                print('> ' + ''.join(lisp.output(exp)))