def isPerfect(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum = sum + i
    
    if sum == n:
        return True
    return False

n = int(input())
if isPerfect(n):
    print("Perfect Number")
else:
    print("Not Perfect Number")