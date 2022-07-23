mine=open('我的發票.txt').read().split()
win=open('中獎號碼.txt').read().split()

sum=0
cnt=0
for i, mine_num in enumerate(mine):
    for win_num in win:
        if mine_num[-5:] == win_num[-5:]:
            print('第',i+1,'張發票對中5碼, 號碼是',win_num[-5:],'!')
            sum+=5000
            cnt+=1
        elif mine_num[-4:] == win_num[-4:]:
            print('第',i+1,'張發票對中4碼, 號碼是',win_num[-4:],'!')
            sum+=4000
            cnt+=1            
        elif mine_num[-3:] == win_num[-3:]:
            print('第',i+1,'張發票對中3碼, 號碼是',win_num[-3:],'!')
            sum+=3000
            cnt+=1
print('共', cnt, "張發票中獎, 合計獎金金額",sum,"元")

print("*"*30)

#另一種寫法
sum=0
cnt=0
for i, mine_num in enumerate(mine):
    for win_num in win:
        for j in range(5,2,-1):
            if mine_num[-j:] == win_num[-j:]:
                print('第',i+1,'張發票對中',j,'碼, 號碼是',win_num[-j:],'!')
                sum+=j*1000
                cnt+=1
                #中斷for 迴圈用break
                break

print('共', cnt, "張發票中獎, 合計獎金金額",sum,"元")
