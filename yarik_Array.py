def max_alternating_sum(test_cases):
        if n == 1:
            return arr[0]
        else:
            ans=arr[0]
            max_ans = ans
            min_ans = 0 if ans > 0 else ans

            for i in range(1, n):
                if abs(arr[i] % 2) != abs(arr[i - 1] % 2):
                    ans+=arr[i]
                else:
                    ans=arr[i]
                    min_ans=0
                max_ans= max(max_ans, ans- min_ans)
                min_ans = min(min_ans, ans)
            return max_ans
        
t=int(input())
for i in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))  
    print(max_alternating_sum(arr))

    
