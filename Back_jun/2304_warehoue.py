'''
1. 


7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''
def test(lst):
    lst1 = []
    temp1 = 0
    for i in range(len(lst)):
        c_h = lst[i][1] 
        if temp1 < c_h:
            temp1 = c_h

        if c_h == mx_h:
            break
        lst1.append(temp1)
    return lst1


n = int(input())
h_lst = []
p_lst = [] # 시작점과 끝점만 가져오면 오케이

mx_h = 0

lst_tmp = []
for _ in range(n):
    p, h = tuple(map(int, input().split()))
    h_lst.append(h)
    p_lst.append(p)
    if mx_h < h:
        mx_h = h

strt = min(p_lst)
end = max(p_lst)
mx_h_cnt = h_lst.count(mx_h)


base = [0]*end

lst = list(zip(p_lst, h_lst))
lst.sort()
cnt = 0
for i in range(strt, end): # end에 +1을 안한 이유는 next를 검사해야하기 때문에
    if i not in p_lst:
        lst.insert(cnt, (0,0))
    cnt+=1


lst1 = test(lst)
# print(lst1)
lst.reverse()
lst2 = test(lst)

total_lst = lst1+lst2
# print(total_lst)
print(sum(total_lst)+(mx_h*mx_h_cnt))


mx = 7
lst = [(1,2), (1,2), (2,2), (3,7), (1,2)]
print(lst.index((3,7)))


for i in range(len(lst)):
    lst[i]