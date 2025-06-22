MOD = 998244353
MAX = 10**6 + 1
def G():
    n = int(input())
    arr = list(map(int, input().split()))
    spf = [0] * MAX
    for i in range(2, MAX):
        if spf[i] == 0:
            spf[i] = i
            for j in range(2 * i, MAX, i):
                if spf[j] == 0:
                    spf[j] = i
    dp = [0] * (n + 1)
    divSum = [0] * MAX
    dp[1] = 1
    val = arr[0]
    primes = []
    while val > 1:
        p = spf[val]
        primes.append(p)
        while val % p == 0:
            val //= p
    divisors = [1]
    for p in primes:
        size = len(divisors)
        for i in range(size):
            if divisors[-1] > 1e6:
                break
            divisors.append(divisors[i] * p)
    for d in divisors:
        if d <= 1e6:
            divSum[d] = (divSum[d] + dp[1]) % MOD
    for i in range(2, n + 1):
        num = arr[i - 1]
        factors = []
        while num > 1:
            p = spf[num]
            factors.append(p)
            while num % p == 0:
                num //= p
        factors = list(set(factors))
        
        k = len(factors)
        result = 0
        for mask in range(1, 1 << k):
            div = 1
            cnt = 0
            for j in range(k):
                if mask & (1 << j):
                    div *= factors[j]
                    cnt += 1
                    if div > 1e6:
                        break
            if div > 1e6:
                continue
            if cnt % 2:
                result = (result + divSum[div]) % MOD
            else:
                result = (result - divSum[div] + MOD) % MOD
        dp[i] = result
        num = arr[i - 1]
        primeFactors = []
        while num > 1:
            p = spf[num]
            primeFactors.append(p)
            while num % p == 0:
                num //= p
        primeFactors = list(set(primeFactors))
        
        divisorsSet = [1]
        for p in primeFactors:
            size = len(divisorsSet)
            for j in range(size):
                if divisorsSet[j] * p > 1e6:
                    continue
                divisorsSet.append(divisorsSet[j] * p)
        for d in divisorsSet:
            if d <= 1e6:
                divSum[d] = (divSum[d] + dp[i]) % MOD
    return dp[n] % MOD
if __name__ == "__main__":
    print(G())
