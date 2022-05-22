
import itertools
from multiprocessing import Pool


from matrix import mat_mul_by_idx

pool = Pool(64)

def one_step_by_idx(s):
    products = itertools.product(s, s)
    new_s = pool.map(mat_mul_by_idx, products)
    return s.union(new_s)


if __name__ == '__main__':
    # Cross-validate the multiplication results
    print(sorted(one_step_by_idx({2, 5, 100})))
