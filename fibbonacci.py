def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    l = fibo(n - 1)
    r = fibo(n - 2)
    result = l + r
    print(f"fibo({n}) = {result}")
    return result
n=int(input())
print(fibo(n))