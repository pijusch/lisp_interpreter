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
            S = lisp.evaluation(exp)
            #print(''.join(lisp.output(lisp.dList)))
            if S:
                print('> ' + ''.join(lisp.output(S)))
            #print('> ' + ''.join(lisp.output(lisp.dList)))
            #print('> ' + ''.join(lisp.output(lisp.get_val(lisp.check_sym_list('ADD'), lisp.dList))))
            #print('> ' + ''.join(lisp.output(lisp.eq(exp,lisp.check_sym_list('T')))))
            # # eval()    To be added in part2
            # if exp:
            #     print('> ' + ''.join(lisp.output(exp)))
