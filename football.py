ss = str(input())

def football(s):
    sev_one = "1111111"
    sev_zero = "0000000"
    if sev_one in s or sev_zero in s:
        return "YES"
    return "NO"

print(football(ss))