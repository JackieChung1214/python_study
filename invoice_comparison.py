mine=open('我的發票.txt').read().split()
win=open('中獎號碼.txt').read().split()
print(win)

for i, num in enumerate(mine):
    if num in win:
        print("第", i+1, "張發票對中號碼", num, "!")