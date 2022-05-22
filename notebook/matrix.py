import numpy as np


class Matrix:
    P = 3

    @classmethod
    def rand(cls):
        m = np.random.randint(Matrix.P, size=(
            Matrix.P, Matrix.P), dtype=np.uint8)
        return cls(m=m)

    def __init__(self, idx=None, m=None):
        if m is not None:
            self.m = m
        elif idx is not None:
            assert 0 <= idx < 19683
            self.m = np.empty(shape=(Matrix.P, Matrix.P), dtype=np.uint8)

            v = idx
            for r in range(Matrix.P):
                for c in range(Matrix.P):
                    self.m[r][c] = v % Matrix.P
                    v = v // Matrix.P

    def idx(self):
        v = 0
        for r in reversed(range(Matrix.P)):
            for c in reversed(range(Matrix.P)):
                v = v * 3
                v += self.m[r][c]
        return v

    def __mul__(self, other):
        new_m = self.m @ other.m % Matrix.P
        return Matrix(m=new_m)

    def __repr__(self):
        return repr(self.m)

    def __str__(self):
        return str(self.m)

    def __hash__(self):
        return hash(tuple(self.m.reshape(-1)))

    def __eq__(self, other):
        return (self.m == other.m).all()


mul_by_idx_cache = np.zeros(pow(3, 18), dtype=np.int32)

def mat_mul_by_idx(i):
    mul_lookup = i[0] * pow(3, 9) + i[1]
    if mul_by_idx_cache[mul_lookup] != 0:
        return mul_by_idx_cache[mul_lookup]
    a = Matrix(idx=i[0])
    b = Matrix(idx=i[1])
    result = (a * b).idx()
    mul_by_idx_cache[mul_lookup] = result
    return result


def print_table(s):
    LINE_WIDTH = pow(3, 4)
    for i in range(pow(3, 9) // LINE_WIDTH):
        l = ''.join(['1' if (i*LINE_WIDTH + j)
                    in s else '0' for j in range(LINE_WIDTH)])
        print(l)


if __name__ == '__main__':
    print(Matrix(0), Matrix(0).idx())
    print(Matrix(1), Matrix(1).idx())

    print('#2 * #2')
    t = Matrix(2)
    print(t, t.idx())
    t = t * t
    print(t, t.idx())

    print(Matrix(19683 - 1), Matrix(19683 - 1).idx())

    t = Matrix(19683 - 1) * Matrix(1)
    print(t, t.idx())
