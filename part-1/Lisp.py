from SExp import SExp
import re


class Lisp:

    def __init__(self):
        self.symbolic_list = []
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

    def eval(self):
        return None

    def input(self, x):
        full_x = []
        while 1:
            if x == '$':
                break
            else:
                full_x.append(x)
            x = input()
        full_x = ' '.join(full_x)

        # Check for errors
        if self.check_bracket(full_x) != 0:
            print('> **error: missing parenthesis**')
            return None
        elif len(full_x) == 0:
            print('> **error: empty**')
            return None
        elif re.search('[^a-z^A-Z^0-9^(^)^.^\s]+', full_x):
            full_x = re.search('[^a-z^A-Z^0-9^(^)^.^\s]+', full_x)
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
            out.append('.')
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
        for i in self.symbolic_list:
            if i.name == string:
                return i

    def update_sym_list(self, atom):
        self.symbolic_list.append(atom)

    def make_tree(self, exp):
        tree = SExp()
        left_par = exp.find('(')
        right_par = exp.rfind(')')

        if left_par == -1 and right_par == -1:
            if re.fullmatch('[0-9]+', exp):
                exp = int(exp)
                tree.type = 0
                tree.val = exp
            else:  # Too general. No Restriction on literals
                if ' ' in exp:
                    print('> **error missing parenthesis**')
                elif '$' in exp:
                    print('> **error: unexpected $**')
                    return None
                elif not re.fullmatch('[A-Z]+[a-zA-Z0-9]*', exp):
                    print('> **error: wrong symbolic ' + exp + '**')
                    return None

                atom = self.check_bracket(exp)

                if atom:
                    tree = atom
                else:
                    tree.type = 1
                    tree.name = exp
                    self.update_sym_list(tree)
        else:
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

    def exp_strip(self,exp):
        return re.sub(' +', ' ', exp).strip()

    def extract_parts(self,exp):
        parts = []  # check end-cases

        while len(exp) > 0:
            ls = exp.find('(')
            if ls == -1:
                parts += exp.split()
                exp = ''
            elif ls == 0:
                r = self.get_the_bracket(ls, exp)
                parts.append(exp[ls:r + 1])
                exp = exp[r + 2:]
            else:
                parts += exp[:ls].split()
                exp = exp[ls:]

        return parts

    def get_the_bracket(i, exp):
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
            if exp[i] == '(':
                c += 1
            elif exp[i] == ')':
                c -= 1
            i += 1
        return c