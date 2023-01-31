import numpy as np

def ex_22():
    cur_mat = np.random.randint(low=1, high=100, size=(5,5))
    print(cur_mat)
    max_val = np.max(cur_mat)
    min_val = np.min(cur_mat)
    print(min_val, max_val)
    cur_mat = np.multiply(cur_mat, 1/max_val)
    print(cur_mat)

def ex_23()

if __name__ == '__main__':
    ex_22()