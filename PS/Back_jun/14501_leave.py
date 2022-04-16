'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

'''
n= int(input())

work = [list(map(int,input().split())) for _ in range(n)]
table = [0]*(n+1)

for i in range(n-1,-1,-1):

    d,p = work[i]

    if i+d <= n:
        table[i] = max(table[d+i]+p, table[i+1])

    else:
        table[i] = table[i+1]

print(table[0])
    


