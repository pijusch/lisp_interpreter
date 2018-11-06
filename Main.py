from Lisp import Lisp

if __name__ == '__main__':
    lisp = Lisp()

    while 1:
        x = raw_input()
        if x == '$$':
            print('> bye!!')
            break
        else:
            exp = lisp.input(x)
            try:
                if exp:
                    S = lisp.evaluation(exp)
                    if S:
                        print('> ' + ''.join(lisp.output(S)))
            except Exception as e:
                print('> error in lisp expression')
                print('> Moving to top level')
