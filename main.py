class IP(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __str__(self):
        return str(self.a) + "." + str(self.b) + "." + str(self.c) + "." + str(self.d)
    def __sub__(self, other):
        a_diff = self.a - other.a
        b_diff = self.b - other.b
        c_diff = self.c - other.c
        d_diff = self.d - other.d
        return IP(a_diff, b_diff, c_diff, d_diff)
    def __add__(self, other):
        a_sum = self.a + other.a
        b_sum = self.b + other.b
        c_sum = self.c + other.c
        d_sum = self.d + other.d
        return IP(a_sum, b_sum, c_sum, d_sum)
