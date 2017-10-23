list = [1, 2, 3, 4, 5]

# 利用 enumerate 產生 tuple (key,value)
for n in enumerate(list):
    print(f'key:{n[0]}-value:{n[1]}')
print('end')

# 以上結果：
# key:0-value:1
# key:1-value:2
# key:2-value:3
# key:3-value:4
# key:4-value:5

# range (1-9 step 2)
for i in range(1, 10, 2):
    print(i)
    # pass
    if i == 3:
        print('pass')
