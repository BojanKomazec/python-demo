import numpy as np

# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
# Return evenly spaced numbers over a specified interval.
def linspace_demo():
    x = np.linspace(-10, 10, 100)
    print(f'type(x) = {type(x)}')
    print(f'x = {x}')

def matrix_demo():
	Y = np.arange(12).reshape(3,4)
	print("Y = ", Y)
	print(Y.shape)
	print(Y.shape[0])
	print(Y.shape[1])

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

def slicing_3d_array_demo():
    # Let's create a 3D matrix by layering these 3 2D matrices one on the top of another.
    # Matrix at index 0 is on the top.
    #
    # Matrix at index 0:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    #
    # Matrix at index 1:
    # 11 22 33
    # 44 55 66
    # 77 88 99
    #
    # Matrix at index 2:
    # 111 222 333
    # 444 555 666
    # 777 888 999
    #
    arr = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
           [[11, 22, 33], [44, 55, 66], [77, 88, 99]],
           [[111, 222, 333], [444, 555, 666], [777, 888, 999]]]
    nparr = np.array(arr)
    print(nparr)

    print(f'nparr.shape = {nparr.shape}') # (3, 3, 3)
    print(f'nparr.shape[:2] = {nparr.shape[:2]}') # get the dimensions of the matrix

    # nparr[m:r:c]
    # m - index of 2D matrix
    # m - index of row in that 2D matrix
    # m - index of column in that 2D matrix
    print(f'nparr[0, 0, 0] = {nparr[0, 0, 0]}') # 1
    print(f'nparr[0, 0, 1] = {nparr[0, 0, 1]}') # 2
    print(f'nparr[2, 1, 1] = {nparr[2, 1, 1]}') # 555

    # If we want to get elements from all columns (entire row will be returned) we can put ':':
    print(f'nparr[2, 1, :] = {nparr[2, 1, :]}')
    # We can omit trailing ':':
    print(f'nparr[2, 1] = {nparr[2, 1]}')

    # If we put : for some dimension that means - all elements in that dimension
    print(f'nparr[:, 1, 2] = {nparr[:, 1, 2]}') # all matrices, row with index 1 and column with index 2: [  6  66 666]
    print(f'nparr[:, :, 2] = {nparr[:, :, 2]}') # all columns with index 2


    print(f'nparr[:, 2, :] = {nparr[:, 2, :]}') # all rows with index 2
    print(f'nparr[:, 2] = {nparr[:, 2]}') # We can omit trailing ':'

    # We can apply 1D slicing syntax on each dimension of 3D matrix.
    # 1D slicing syntax: [b:e:s]
    # b - index of the element where to begin from
    # e - index of the element where to stop (exclusive)
    # s - step
    # [:2] - elements with index 0 and 1
    print(f'nparr[:2, :, :] = {nparr[:2, :, :]}') # matrices with index 0 and 1
    print(f'nparr[:2] = {nparr[:2]}') # same as above

def two_arrays_to_tuples_array_demo():
    pass

def numpy_demo():
    linspace_demo()
    # zeros_demo()
    # ndarray_sum_demo()
    # slicing_3d_array_demo()
