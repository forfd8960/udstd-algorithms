
# https://stackoverflow.com/questions/5246856/how-did-python-implement-the-built-in-function-pow

"""
At its core, the idea of the algorithm is rather simple, though. Let's say we want to compute a ** b for positive integers a and b, and b has the binary digits b_i. Then we can write b as

b = b_0 + b1 * 2 + b2 * 2**2 + ... + b_k ** 2**k
ans a ** b as

a ** b = a**b0 * (a**2)**b1 * (a**2**2)**b2 * ... * (a**2**k)**b_k
Each factor in this product is of the form (a**2**i)**b_i. 
If b_i is zero, we can simply omit the factor. If b_i is 1, 
the factor is equal to a**2**i, and these powers can be computed for all i by repeatedly squaring a. 
Overall, we need to square and multiply k times, where k is the number of binary digits of b.
"""


def my_pow(a, n):
    n_bin = bin(n)
    n_bin = n_bin[2:]
    
    n_bin = [int(x) for x in reversed(n_bin)]
    
    result = 1
    for i in range(0, len(n_bin)):
        result *= pow(pow(a, pow(2, i)), n_bin[i])

    return result

"""
>>> from pow import my_pow
>>> my_pow(5, 3)
125
>>> my_pow(2, 3)
8
>>> my_pow(3, 3)
27
>>> my_pow(2, 10)
1024
"""