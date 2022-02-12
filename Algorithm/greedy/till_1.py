'''
어떤 수 N이 1이 될때까지 
1번 과정: N 을 1을 뺸다
2번 과정: N을 K로 나눈다

2678 , 80
33, 2678 - 2640 = 38

33+38 = 71 + 1

17 // 4 = 4
17 % 4 = 1

1. 나누어서 나머지가 0이 나오면 빼고
2. 나누어떨어지면 그때 나눈다

'''

n, k = map(int,input().split())

cnt = 0
while n > 1:

    if n % k == 0:
        n = n//k
        cnt += 1

    else:
        n -= 1
        cnt += 1

    

print(cnt)