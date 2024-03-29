"""

The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return

[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(m) being the smallest one such as F(m) * F(m+1) > prod.

"""

def productFib(prod):
    # your code  
    fib_list = Fib(prod, 0, 1)
    j = 0
    i = 0
    for i in range(1, len(fib_list)):
        if (fib_list[i - 1] * fib_list[i]) == prod:
            return [fib_list[i - 1], fib_list[i], True]
        elif (fib_list[i - 1] * fib_list[i]) > prod:
            return [fib_list[i - 1], fib_list[i], False]
    
def Fib(prod, n1, n2):
    p = prod ** 0.5
    i = 0
    l = []
    while i < int(p):
        l.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1
        
    return l
