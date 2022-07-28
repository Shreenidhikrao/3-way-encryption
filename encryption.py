import math
import numpy as np

def encrypt_str(str): 
    n = []
    for x in str:
        n.append(ord(x) - 96)
    
    print("Ascii encryption  :",n)
    return n

def encrypt_rsa(arr):
    k=[]
    p = 3
    q = 7
    e = 2
    n = p*q
    for i in range(len(arr)): 
        en = math.pow(arr[i],e)     
        c = en % n
        k.append(c)
    print("RSA encryption :",k)
    return k

def split_arr(arr_) -> list:
    arr = arr_.copy()
    arr = [int(x) for x in arr]
    i = 0
    result = []
    length = len(arr)
    if length % 3 != 0:
        while (len(arr) % 3)!=0:
            arr.append(0)
    while i < length:
        temp = [arr[i] , arr[i+1], arr[i+2]]
        result.append(temp)
        i = i + 3
    return result

def encrypt_matrix(arr):
    mat = [[1,2,1],[-1,-1,0],[1,0,0]]
    res = []
    for i in range(len(arr)):
        res.append(np.dot(arr[i] , mat))
    #print("finally encrypted array",res)
    return res

def decrypt_matrix(arr):
    inv_mat = []
    res = []
    mat = [[1,2,1],[-1,-1,0],[1,0,0]]
    inv_mat = np.linalg.inv(mat)
    for i in range(len(arr)):
        res.append(np.dot(arr[i] , inv_mat))
    print("Decrypted array" , res)

def decrypt_rsa(arr):
    k=[]
    p = 3
    q = 7
    e = 2
    n = p*q
    d = 1/3 % ((p-1)*(q-1))
    for i in range(len(arr)):
        m = math.pow(arr[i] , d)
        decr = m % n 
        k.append(decr)
    return k

def listToString(s): 
    str1 = ""     
    return (str1.join(s))

def decrypt_str(arr):
    n = []
    for x in arr:
        n.append(chr(x + 96))    
    print("Original string:",listToString(n))
    return n


str = input("Please give a string for encryption :")
arr = []
arr1 = []
arr2 = []
arr3 = []
arr = encrypt_str(str)
arr1 = encrypt_rsa(arr)
arr2 = split_arr(arr1)
arr3 = encrypt_matrix(arr2)
print("Finally encrypted array",arr3)
decrypt_matrix(arr3)
print("RSA decryption:" , arr)
decrypt_rsa(arr1)
decrypt_str(arr)