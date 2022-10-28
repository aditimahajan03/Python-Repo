# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 17:18:12 2022

@author: Aditi
"""

# python program to demonstrate hamming code


def calcRedundantBits(m):

    # use formula 2^r >= m+r+1
    # to calculate the number of redundant bits.
    # iterate over 0... m and return the value
    # that satisfies the question

    for i in range(m):
        if(2**i >= m+i+1):
            return i

def posRedundantBits(data, r):

    # redundancy bits are placed at the positions
    # which correspond to the power of 2.
    j = 0
    k = 1
    m = len(data)
    res = ''

    # if position is power of 2 then insert'0'
    # else appeend the data
    for i in range(1, m +r+1):
        if(i == 2**j):
            res = res +'0'
            j += 1
        else:
            res = res + data[-1*k]
            k += 1

    # the result is reversed since positions are
    # counted backwards.(m+r+1,... 1)
    return res[::-1]

def calcParityBits(arr, r):
    n = len(arr)

    # for finding rth parity bit, iterate over
    # 0 to r-1
    for i in range(r):
        val = 0
        for j in range(1, n+1):

            # if position has 1 in ith significant
            # position then BITWISE OR the array value
            #to find parity bit value.
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1*j])
                # -1 * j is given since array is reversed
        
        # string concatenation
        # (0 to n - 2^r) + parity bit + (n-2^r + 1 to n)
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2*i)+1:]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0

    # calculate parity bits again
    for i in range(nr):
        val = 0
        for j in range(1, n+1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1*j])
        # create a binary number by appending
        # parity bitrts together
        res = res + val*(10**i)
    # convert binary to decimal
    return int(str(res), 2)

# enter the data to be transmitted
data = input("enter the data to be transmitted: ")

# calculate the number of redundant bits required
m = len(data)
r = calcRedundantBits(m)

# determine the positions of redundant bits
arr = posRedundantBits(data, r)

# determine the parity bits
arr = calcParityBits(arr, r)

# data to be transferred
print("Data transferred is '"+ arr)

# stimulate error in transmission by changing
# a bit value
# 10101001110 -> 11101001110, error in 10th position.

arr = '11101001110'
print("Error data is " + arr)
correction = detectError(arr, r)
if (correction==0):
    print("there is no error in the recieved message.")
else:
    print("The position of error is ", len(arr)-correction+1, "from the left")

print("Redundant bits = " + str(calcRedundantBits(r)))
print("Parity bits: " + str(calcParityBits(arr, r)))
