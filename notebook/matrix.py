import numpy as np

class Matrix:
    P = 3
    
    @classmethod
    def rand(cls):
        m = np.random.randint(Matrix.P, size=(Matrix.P, Matrix.P), dtype=np.uint8)
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


def mat_mul_by_idx(i):
    a = Matrix(idx = i[0])
    b = Matrix(idx = i[1])
    return (a * b).idx()

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