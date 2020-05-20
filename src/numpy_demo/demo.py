import numpy as np

def zeros_demo():
    # zeros cretaes rowxcolumn matrix and fills it with zeros
    # float32 zero is in form 0.
    arr1 = np.zeros((4, 2), dtype = "float32")

    # ndarray.shape - returnd array shape/dimensions
    print("arr1.shape = ", arr1.shape) # (4, 2)

    print("arr1 = ", arr1)

# numpy.ndarray.sum
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.sum.html#numpy.ndarray.sum
def ndarray_sum_demo():
    arr = np.zeros((3, 2))
    arr[0, 0] = 1
    arr[0, 1] = 2
    arr[1, 0] = 3
    arr[1, 1] = 4
    arr[2, 0] = 5
    arr[2, 1] = 6

    print("arr = ", arr)
    # arr =  [[1. 2.]
    #         [3. 4.]
    #         [5. 6.]]

    sum_all = arr.sum()
    print("sum_all = ", sum_all)

    # This is a 2D array so we have two axises, with index 0 and 1
    # axis = 0 is vertical (columns); sum(axis = 0) calculates sum for each column
    sum_axis_0 = arr.sum(axis = 0)
    print("sum_axis_0 = ", sum_axis_0) # [ 9. 12.]

    # axis = 1 is horisontal (rows); sum(axis = 1) calculates sum for each row
    sum_axis_1 = arr.sum(axis = 1)
    print("sum_axis_1 = ", sum_axis_1) # [ 3.  7. 11.]



def numpy_demo():
    # zeros_demo()
    ndarray_sum_demo()
