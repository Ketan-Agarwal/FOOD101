import numpy as np


def calc_det(arr):
    det = 0
    if arr.shape[0] > 2:
        for j in range(arr.shape[0]):
            element = np.multiply(((-1)**j)*arr[0][j],calc_det(np.delete(arr[1:], j, 1)), dtype=object)
            det += element
        return det
    else:
        return arr[0][0]*arr[1][1] - arr[0][1]*arr[1][0]

def calc_dot(arr1, arr2):
    res = []
    for i in range(arr1.shape[0]):
        for j in range(arr1.shape[1]):
            res.append(arr1[i][j]*arr2[i][j])
    result = np.array(res)
    return result.reshape(arr1.shape[0], arr1.shape[1])



def calc_matmul(arr1, arr2):
    # order of arr1 and arr2 respectively --- n1*m, m*n2
    n1 = arr1.shape[0]
    m = arr1.shape[1]
    n2 = arr2.shape[1]
    res = []
    for i in range(n1):
        for j in range(n2):
            sum = 0
            for k in range(m):
                sum += arr1[i][k]*arr2[k][j]
            res.append(sum)
    result = np.array(res)
    result = result.reshape(n1, n2) # since elements appended are row wise, array can directly be reshaped into required shape since the elements are exactly as required
    return result


def matrix_operation(array1, array2, operation):
    if operation == 'dot' and array1.shape == array2.shape:
        return calc_dot(array1, array2)

    elif operation == 'dot' and array1.shape != array2.shape:
        print("Cannot perform dot product, since shape of matrix is not same")

    elif operation == "matrix":
        result_using_npfunc = np.matmul(array1, array2) if array1.shape[1] == array2.shape[0] else None
        errmsg = f"Cannot Do matrix multiplication, make sure Cols of 1st matrix == Rows of 2nd matrix. ({array1.shape[1]} != {array2.shape[0]}) LOL"

        if result_using_npfunc is not None:
            return result_using_npfunc
        else:
            return errmsg

    elif operation == "determinant":
        det1 = calc_det(array1) if array1.shape[0] == array1.shape[1] else None
        det2 = calc_det(array2) if array2.shape[0] == array2.shape[1] else None
        if det1 is None and det2 is None:
            return "NaN", "NaN"
        elif det1 is None:
            return "NaN", float(det2)
        elif det2 is None:
            return float(det1), "NaN"
        else:
            return float(det1), float(det2)

    else:
        return None

arr1 = np.array([[1.7,2.3],[-9.5,3.3]], dtype=np.float64)
arr2 = np.array([[2,3,1],[1,2,3],[4,5,6]], dtype=np.float64)
#arr1 = np.random.rand(10,10)
#arr2=np.random.randint(0,99,(10,10))
#arr2 = np.array(arr2, dtype=np.float64)
print(matrix_operation(arr1, arr2, "determinant"))