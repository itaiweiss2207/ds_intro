import random
import timeit

import numpy as np
import datetime as dt


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
    import warnings
    warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)
def ex_32():
    print(np.sqrt(-1) == np.emath.sqrt(-1))

def ex_33():
    yesterday = dt.datetime.now() + dt.timedelta(-1)
    print(yesterday)
    today = dt.datetime.now()
    tomorrow = dt.datetime.now() + dt.timedelta(days=1)
    print(today)
    print(tomorrow)
def ex_34():
    start_of_july_2016 = dt.datetime(2016,7,1)
    end_of_july_2016 = dt.datetime(2016,7,31)
    all_dates_in_range = np.arange(start_of_july_2016.date(), end_of_july_2016.date())
    print(all_dates_in_range)

def ex_35():
    A = np.random.randint(low=-10, high= 20, size=(3,3))
    B = np.random.randint(low=-10, high=20, size=(3, 3))

    print(A)
    for row in range(len(A)):
        for element in range(len(A[row])):
            A[row][element] = (A[row][element] + B[row][element]) *(-A[row][element] / 2)
    print(A)


def ex_36():
    mat = np.random.random(size=(3,3))
    print(mat)

    # method_1
    mat_1 = mat//1
    print(mat_1)

    # method_2
    mat_2 = np.floor(mat)
    print(mat_2)

    # method_3
    mat_3 = mat.astype(int)
    print(mat_3)

    #method_4
    mat_4 = np.int_(mat)
    print(mat_4)


def ex_37():
    mat = np.random.randint(low=-10, high=20, size=(5,5))
    row_value = np.sum(mat[0])
    for i, row in enumerate(mat[1:]):
        while np.sum(row) != row_value:
            row = np.random.randint(low=-10, high=20, size=(1,5))
            mat[i] = row
    print(mat)

def int_gen():
    for i in range(10):
        yield random.randint(1, 20)

def ex_38():
    for i in int_gen():
        print(i)
    mat = np.array([])
    for i in int_gen():
        mat = np.append(mat, np.array([i]), axis=0)


def ex_39():
    exc = [0.0,1.0]
    mat = np.random.uniform(0.0, 1.0, size=10)
    while 0.0 in mat or 1.0 in mat:
        mat = np.random.uniform(0.0, 1.0, size=10)
    print(mat)

def ex_40():
    mat = np.random.randint(1,20, 10)
    mat.sort()
    print(mat)

def ex_41():
    mat = np.random.randint(1, 20, 10)
    sum_1 = sum(mat)
    sum_2 = mat.sum()
    print(sum_1, sum_2)

def ex_42():
    mat_1 = np.random.randint(1, 20, 10)
    mat_2 = np.random.randint(1, 20, 10)
    print(mat_1, mat_2)
    print(all(mat_1 == mat_2))

def ex_43():
    mat = np.arange(10)
    mat.setflags(write=False)
    print(mat)

def ex_44():
    coord_in_cartes = np.random.random((10,2))
    radius = [np.hypot(cor[0], cor[1]) for cor in coord_in_cartes]
    angle = [np.arctan2(cor[1], cor[0]) for cor in coord_in_cartes]
    result = np.column_stack((radius, angle))
    print(result)


def ex_45():
    vector = np.random.random(10)
    print(vector)
    max_value = np.max(vector)
    for i, entry in enumerate(vector):
        if entry == max_value:
            vector[i] = 0
    print(vector)


def ex_46(x, y):
    balanced_mat = np.array([[(i*(1/x), (1-j*(1/y))) for i in range(x)] for j in range(y)])
    print(balanced_mat)

def ex_47(X, Y):
    C = np.zeros((len(X), len(Y)))
    for i, Xi in enumerate(X):
        for j, Yj in enumerate(Y):
            C[i][j] = 1/(Xi - Yj)
    print(C)


def ex_50():
    vector = np.array([1, 3, 5, 7, 9])
    scalar = 6
    index = np.abs(vector - scalar).argmin()
    closest_value = vector[index]
    print(closest_value)



if __name__ == '__main__':
    ex_49()
