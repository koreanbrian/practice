#n,k 입력
n, k = map(int,input().split())
result = 0

while n >= k:
    while n%k != 0:
        n = n-1
        result = result +1
    n= n/k

while n>1:
    n = n-1
    result = result +1

print (result)