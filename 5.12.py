import numpy as np

b, n, a = 2, 10, 0
delx = (b -a)/ n

def trapezoidal_method(x):
    integral_used = float(x ** 4 - 2 * x + 1)
    return integral_used


def trapezodal_sums(n):
    sum = 0
    first_part = 0.5 * trapezoidal_method(0) + 0.5 *trapezoidal_method(1)
    for k in range(1,10):
        x = a + k * delx
        sum = sum + trapezoidal_method(x)
    return(2*delx * (first_part + sum))

def simp_method(x):
    integral_used = float(x ** 4 - 2 * x + 1)
    return integral_used


def simp_sums(n):
    simp_sum_one = 0
    simp_sum_two = 0
    first_part_simp = 1/3 * (simp_method(0) + simp_method(2))
    for k in range(0,n):
        simp_sum_one = 4 * simp_sum_one + simp_method(a + (2 * k - 1)* delx)
        simp_sum_two = 2 * simp_sum_two * simp_method(a + 2 * (k/2-1) * delx)
    return(simp_sum_one + simp_sum_two + first_part_simp)


print(trapezodal_sums(1000))
print(simp_sums(100))

## The  estimates for both trapezoidal and Simpsons rule are close but not close
## enough to the known constant








