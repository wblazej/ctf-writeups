N = int(input()) 
x = divisors(GaussianIntegers()(N))

for xx in x:
    p = abs(int(xx.real()))
    q = abs(int(xx.imag()))

    if is_prime(p) and is_prime(q) and pow(p, 2) + pow(q, 2) == N:
        print(p, q)
