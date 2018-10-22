class SExp:

    def __init__(self):
        self.type = None  # 0 = int, 2 = literal, 3 = non-atomic
        self.val = None
        self.name = None
        self.left = None
        self.right = None
