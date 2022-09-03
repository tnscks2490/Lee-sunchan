import sys

N = int(sys.stdin.readline())

def fib(N):
    if N == 1 or N == 2:
        return 1
    else:
        return (fib(N-1) + fib(N-2))
f = [0] * (N+3)
def fibonacci(N):
    f[1] = f[2] = 1
    for i in range(3,N+1):
        f[i] = f[i-1] + f[i-2]
    return N-2

a = fib(N)
b = fibonacci(N)
print(a,b)