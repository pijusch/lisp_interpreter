from SExp import SExp
import re


class Lisp:

    def __init__(self):
        self.symbolicList = []
        self.pList = [] # primitive functions

        self.pList.append('CAR')
        self.pList.append('CDR')
        self.pList.append('CONS')
        self.pList.append('ATOM')
        self.pList.append('NULL')
        self.pList.append('EQ')

        # NIL atom
        nil = SExp()
        nil.type = 1
        nil.name = 'NIL'
        self.update_sym_list(nil)

        # T atom
        tee = SExp()
        tee.type = 1
        tee.name = 'T'
        self.update_sym_list(tee)

        # COND atom
        tee = SExp()
        tee.type = 1
        tee.name = 'COND'
        self.update_sym_list(tee)

        # QUOTE atom
        tee = SExp()
        tee.type = 1
        tee.name = 'QUOTE'
        self.update_sym_list(tee)

        # DEFUN atom
        tee = SExp()
        tee.type = 1
        tee.name = 'DEFUN'
        self.update_sym_list(tee)

        # CDR atom
        tee = SExp()
        tee.type = 1
        tee.name = 'CDR'
        self.update_sym_list(tee)

        # CAR atom
        tee = SExp()
        tee.type = 1
        tee.name = 'CAR'
        self.update_sym_list(tee)

        # CAR atom
        tee = SExp()
        tee.type = 1
        tee.name = 'CONS'
        self.update_sym_list(tee)

        # CAR atom
        tee = SExp()
        tee.type = 1
        tee.name = 'ATOM'
        self.update_sym_list(tee)

        # CAR atom
        tee = SExp()
        tee.type = 1
        tee.name = 'NULL'
        self.update_sym_list(tee)

        # CAR atom
        tee = SExp()
        tee.type = 1
        tee.name = 'EQ'
        self.update_sym_list(tee)

        # CAR atom
        tee = SExp()
        tee.type = 1
        tee.name = 'PLUS'
        self.update_sym_list(tee)

        # CAR atom
        tee = SExp()
        tee.type = 1
        tee.name = 'MINUS'
        self.update_sym_list(tee)

        self.dList = self.check_sym_list('NIL')

    def evlis(self, exp, alist):
        if self.null(exp).name == 'T':
            return self.check_sym_list('NIL')
        else:
            return self.cons(self.eval(self.car(exp), alist), self.evlis(self.cdr(exp), alist))

    def plus(self, exp1, exp2):
        if exp1.type == 0 and exp2.type == 0:
            temp = SExp()
            temp.type = 0
            temp.val = exp1.val + exp2.val
            return temp
        else:
            print('wrong with plus')
            return None

    def minus(self, exp1, exp2):
        if exp1.type == 0 and exp2.type == 0:
            temp = SExp()
            temp.type = 0
            temp.val = exp1.val - exp2.val
            return temp
        else:
            print('wrong with minus')
            return None

    def evcon(self, exp, alist):
        if self.null(exp).name == 'T':
            print('No condition satisfies')
            return None
        elif self.eval(self.car(self.car(exp)), alist).name == 'T':
            return self.eval(self.car(self.cdr(self.car(exp))), alist)
        else:
            return self.evcon(self.cdr(exp), alist)

    def in_(self, exp, alist):
        if self.null(alist).name == 'T':
            return self.check_sym_list('NIL')
        elif self.eq(self.car(self.car(alist)), exp).name == 'T':
            return self.check_sym_list('T')
        else:
            return self.in_(exp, self.cdr(alist))

    def get_val(self, exp, alist):
        if self.eq(self.car(self.car(alist)), exp).name == 'T':
            return self.cdr(self.car(alist))
        else:
            return self.get_val(exp, self.cdr(alist))

    def eval(self, exp, alist):
        print(''.join(self.output(alist)))
        if self.atom(exp).name == 'T':
            if self.int_(exp).name == 'T':
                return exp
            elif self.eq(exp, self.check_sym_list('T')).name == 'T':
                return self.check_sym_list('T')
            elif self.eq(exp, self.check_sym_list('NIL')).name == 'T':
                return self.check_sym_list('NIL')
            elif self.in_(exp, alist).name == 'T':
                return self.get_val(exp, alist)
            else:
                print('unbounded atom')
                return None
        elif self.atom(self.car(exp)).name == 'T':
            if self.eq(self.car(exp), self.check_sym_list('QUOTE')).name == 'T':
                return self.car(self.cdr(exp))
            elif self.eq(self.car(exp), self.check_sym_list('COND')). name == 'T':
                return self.evcon(self.cdr(exp), alist)
            else:
                #print(''.join(self.output(self.evlis(self.cdr(exp), alist))))
                return self.apply(self.car(exp), self.evlis(self.cdr(exp), alist), alist)
        else:
            print('not a lisp expression')
            return None

    def addpairs(self, arg, x, alist):
        ralist = SExp()
        temp = ralist
        temp.type = 2
        while 1:
            temp.left = self.cons(self.car(arg), self.car(x))
            arg = self.cdr(arg)
            x = self.cdr(x)
            if arg.type != 2:
                temp.right = alist
                break
            temp.right = SExp()
            temp.right.type = 2
            temp = temp.right

        return ralist


    def apply(self, f, x, alist):
        if self.atom(f).name == 'T':
            if self.eq(f, self.check_sym_list('CAR')).name == 'T':
                return self.car(self.car(x))
            elif self.eq(f, self.check_sym_list('CDR')).name == 'T':
                return self.cdr(self.car(x))
            elif self.eq(f, self.check_sym_list('CONS')).name == 'T':
                return self.cons(self.car(x), self.cdr(x))
            elif self.eq(f, self.check_sym_list('ATOM')).name == 'T':
                return self.atom(self.car(x))
            elif self.eq(f, self.check_sym_list('NULL')).name == 'T':
                return self.null(self.car(x))
            elif self.eq(f, self.check_sym_list('EQ')).name == 'T':
                return self.eq(self.car(x), self.car(self.cdr(x)))
            elif self.eq(f, self.check_sym_list('MINUS')).name == 'T':
                return self.minus(self.car(x), self.car(self.cdr(x)))
            elif self.eq(f, self.check_sym_list('PLUS')).name == 'T':
                return self.plus(self.car(x), self.car(self.cdr(x)))
            else:
                return self.eval(self.cdr(self.get_val(f, self.dList)), self.addpairs(self.car(self.get_val(f, self.dList)), x, alist))
        else:
            print('not a lisp expression')
            return None

    def add2dList(self, exp):

        temp = SExp()
        temp.type = 2
        temp.left = self.car(self.car(exp))
        temp.right = SExp()
        temp.right.type = 2
        temp.right.left = self.cdr(self.car(exp))
        temp.right.right = self.car(self.cdr(exp))

        temp2 = SExp()
        temp2.type = 2
        temp2.left = temp
        temp2.right = self.dList
        self.dList = temp2

    def evaluation(self, exp):
        if exp.type == 2 and self.car(exp) == self.check_sym_list('DEFUN'):
            self.add2dList(self.cdr(exp))
            return self.car(self.car(self.cdr(exp)))
        else:
            return self.eval(exp, self.check_sym_list('NIL'))

    def car(self, exp):
        if exp.type == 2:
            return exp.left
        else:
            print('CAR received an atom')

    def eq(self, exp1, exp2):
        if exp1.type == 1 and exp2.type == 1 and exp1.name == exp2.name or exp1.type == 0 and exp2.type == 0 and exp1.val == exp2.val:
            return self.check_sym_list('T')
        else:
            return self.check_sym_list('NIL')

    def cdr(self, exp):
        if exp.type == 2:
            return exp.right
        else:
            print('CDR received an atom')
            return None

    def atom(self, exp):
        if exp.type > 1:
            return self.check_sym_list('NIL')
        else:
            return self.check_sym_list('T')

    def cons(self, exp1, exp2):
        rtemp = SExp()
        rtemp.left = exp1
        rtemp.right = exp2
        rtemp.type = 2

        return rtemp

    def null(self, exp):
        if exp == self.check_sym_list('NIL'):
            return self.check_sym_list('T')
        else:
            return self.check_sym_list('NIL')

    def int_(self, exp):
        if exp.type == 0:
            return self.check_sym_list('T')
        else:
            return self.check_sym_list('NIL')

    def input(self, x):
        full_x = []
        while 1:
            if x == '$':
                break
            else:
                full_x.append(x)
            x = raw_input()
        full_x = ' '.join(full_x)

        # Check for errors
        if self.check_bracket(full_x) != 0:
            print('> **error: missing parenthesis**')
            return None
        elif len(full_x) == 0:
            print('> **error: empty**')
            return None
        elif re.search('[^a-z^A-Z^0-9^(^)^.^\s^-]+', full_x):
            full_x = re.search('[^a-z^A-Z^0-9^(^)^.^\s^-]+', full_x)
            print('> **error unexpected ' + full_x.group() + '**')
            return None

        tree = self.make_tree(full_x)

        return tree

    def output(self,tree):
        out = list()
        if tree.type == 2:
            out.append('(')
            if tree.left:
                out += self.output(tree.left)
            out.append(' . ')
            if tree.right:
                out += self.output(tree.right)
            out.append(')')
        else:
            if tree.type == 0:
                out.append(str(tree.val))
            else:
                out.append(tree.name)
        return out

    def check_sym_list(self, string):
        for i in self.symbolicList:
            if i.name == string:
                return i
        return None

    def update_sym_list(self, atom):
        self.symbolicList.append(atom)

    def make_tree(self, exp):
        exp = self.exp_strip(exp)
        tree = SExp()
        left_par = exp.find('(')

        if left_par == -1: # Its atomic
            if self.fullmatch('-?[0-9]+', exp):
                exp = int(exp)
                if abs(exp) > 999999:
                    print('> **error: illegal integer**')
                    return None
                tree.type = 0
                tree.val = exp
            else:
                if ' ' in exp:
                    print('> **error missing parenthesis**')
                    return None
                elif '$' in exp:
                    print('> **error: unexpected $**')
                    return None
                elif not self.fullmatch('[A-Z]+[A-Z0-9]*', exp):
                    print('> **error: illegal symbolic ' + exp + '**')
                    return None
                elif len(exp) > 10:
                    print('> **error: illegal symbolic ' + exp + '**')
                    return None

                if self.check_sym_list(exp):
                    tree = self.check_sym_list(exp)
                else:
                    tree.type = 1
                    tree.name = exp
                    self.update_sym_list(tree)

        else:
            right_par = self.get_the_bracket(left_par,exp)
            if len(exp[right_par+1:].strip()) != 0 or len(exp[:left_par].strip())!=0:
                print('> **error missing parenthesis')
                return None
            tree.type = 2
            exp = self.exp_strip(exp[left_par + 1:right_par])
            parts = self.extract_parts(exp)
            if '.' in parts:
                if len(parts) == 3 and parts[1] == '.':
                    tree.left = self.make_tree(parts[0])
                    tree.right = self.make_tree(parts[2])
                    if not (tree.left and tree.left):
                        return None
                else:
                    print("> **error: unexpected dot**")
                    return None
            elif len(parts) > 0:
                temp = tree
                for i in parts[:-1]:
                    temp.left = self.make_tree(i)
                    if not temp.left:
                        return None
                    temp.right = SExp()
                    temp = temp.right
                    temp.type = 2
                temp.left = self.make_tree(parts[-1])
                if not temp.left:
                    return None
                temp.right = self.check_sym_list('NIL')
            else:
                tree.type = 1
                tree = self.check_sym_list('NIL')

        return tree

    def exp_strip(self, exp):
        return re.sub(' +', ' ', exp).strip()

    def extract_parts(self, exp):
        parts = []  # check end-cases

        while len(exp) > 0:
            ls = exp.find('(')
            if ls == -1:
                parts += exp.split()
                exp = ''
            elif ls == 0:
                r = self.get_the_bracket(ls, exp)
                parts.append(exp[ls:r + 1])
                exp = exp[r + 1:]
            else:
                parts += exp[:ls].split()
                exp = exp[ls:]

        #nparts = []

        #for i in parts:
         #   if i != '.':
         #       temp = i.split('.')
         #       if len(temp[0]) !=0 :
         #           nparts.append(temp[0])
         #       for j in temp[1:]:
         #           if len(j) != 0:
         #               nparts += ['.', j]
         #   else:
         #       nparts.append('.')

        return parts

    def get_the_bracket(self, i, exp):
        j = i
        c = 1
        while c != 0:
            j += 1
            if exp[j] == '(':
                c += 1
            elif exp[j] == ')':
                c -= 1

        return j

    def check_bracket(self, exp):
        c = 0
        i = 0
        while i < len(exp):
            if c < 0:
                return -1
            if exp[i] == '(':
                c += 1
            elif exp[i] == ')':
                c -= 1
            i += 1
        return c

    def fullmatch(self,pat,string):
        if re.match(pat,string):
            if re.match(pat,string).group(0) == string:
                return True
            else:
                return False
        else:
            return False
