
import itertools
import random
from multiprocessing import Pool

from matrix import mat_mul_by_idx

pool = Pool(64)

# 1 million matmul a batch
_MAX_SAMPLES = 1_000_000


def one_step_by_idx(s):
    products = list(itertools.product(s, s))
    subset = random.sample(products, k=min(_MAX_SAMPLES, len(products)))
    new_s = pool.map(mat_mul_by_idx, subset)
    return s.union(new_s)


if __name__ == '__main__':
    # Cross-validate the multiplication results
    print(sorted(one_step_by_idx({2, 5, 100})))
