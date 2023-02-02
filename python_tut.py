import numpy as np


def ex_22():
    cur_mat = np.random.randint(low=1, high=100, size=(5,5))
    print(cur_mat)
    max_val = np.max(cur_mat)
    min_val = np.min(cur_mat)
    print(min_val, max_val)
    cur_mat = np.multiply(cur_mat, 1/max_val)
    print(cur_mat)

def ex_23():
    color_type = np.dtype([('R', np.ubyte, 1),('G', np.ubyte, 1),('B', np.ubyte, 1),('A', np.ubyte, 1)])
    color_vector = np.array([5], dtype=color_type)
    print(color_vector)

def ex_24():
    five_three_mat = np.random.randint(1,10,(5,3))
    three_two_mat = np.random.randint(1, 10, (3,2))
    product = np.matmul(five_three_mat,three_two_mat)
    print(product)

def ex_25():
    vector = np.random.randint(low=1,high=10,size=(20))
    print(vector)
    for i, element in enumerate(vector):
        if element >= 3 and element <= 8:
            vector[i] = 0
    print(vector)


def ex_27():
    Z = np.random.randint(low=1, high=10, size=(20))
    a = Z ** Z
    b = 2 << Z >> 2
    c = Z < - Z
    d = 1j * Z
    e = Z / 1 / 1
    print(Z,a,b,c,d,e)

def ex_29():
    vector = np.random.uniform(low=-2, high=4, size=(20))
    print(vector)
    rounded = [np.floor(element) if (element < 0) else
               np.ceil(element) for element in vector]
    rounded = np.array(rounded)
    print(rounded)

def ex_30():
    vector1 = np.random.randint(low=-5, high=20, size=(20))
    vector2 = np.random.randint(low=-5, high=20, size=(20))
    common_vec = np.array([value for value in vector1 if value in vector2])
    print(vector1)
    print(vector2)
    print(common_vec)

def ex_31():


if __name__ == '__main__':
    ex_30()