'''
벨류값이 들어가면
반대편의 인덱스 값의 벨류가 나왔으면 좋겠어
'''
# 다이스 값은 리스트다

def route(dice, idx):

    if idx == 0:
        return dice[-1]

    elif idx == 1:
        return dice[-3]

    elif idx == 2:
        return dice[-2]

    elif idx == 3:
        return dice[-5]

    elif idx == 4:
        return dice[-4]

    elif idx == 5:
        return dice[-6] 

# lst = [2 ,3 ,1 ,6 ,5 ,4]
# print(route(lst, lst.index(5)))
# 리스트에서 값을 삭제
# 그 리스트에서 최대값을 구해서 계속 더함
# 그리고 totaㅣ 값을 구해
# 그 안에서 바로 max함수 구현
# 답
'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
'''


num = int(input())
dices = []

for i in range(num):
    d = list(map(int, input().split()))
    dices.append(d)
# frist_dice = 

result = 0
for i in dices[0]:
    
    total = 0
    st_val = i
    for dice in dices:
        lst = []
        op_value = route(dice, dice.index(st_val))
        # print(dice)
        # print('op:',op_value)
        # print('st:', st_val)

        for j in dice:
            if j != op_value and j != st_val:
                lst.append(j)

        mx_dice = max(lst)
        total += mx_dice

        lst = []
        st_val = op_value
        

    # print('-'*30)
    
    if  result < total:
        result = total

print(result)

        
        



# lsttest = [2, 3, 1, 6, 5, 4]

# print(lsttest[0])         #2
# print(lsttest.index(2))   #0