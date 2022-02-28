import numpy as np
import time

def del_function(x):
    return x * (x - 1)

delta = np.array([1e-2, 1e-4, 1e-6,1e-8])

x = 1
for h in delta:
    ans =(del_function(x+delta)-del_function(x))/h
print(ans)

def integral_calculator_two(n):
    h = 2/n
    answer = 0
    for k in range(1,n):
        xk = -1 + h * k
        yk = np.sqrt(1 - xk**2)
        answer = answer+ yk*h
    return answer
	
	
print(integral_calculator_two(100))
print(integral_calculator_two(10000))
print(integral_calculator_two(200))

start=time.time()
integral_calculator_two(100)
end=time.time()
print(f"Program took :{end-start} seconds to run")
