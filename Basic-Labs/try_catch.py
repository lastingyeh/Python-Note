
try:
    file = open('file_txt.txt', 'r+')
except Exception as e:
    print('file is not found', e)

    res = input('do you want to create a new file:')

    print(res)

    if res == 'y':
        file = open('file_txt.txt', 'w')
    else:
        pass
else:
    file.write('write string to file_txt.txt')
file.close()
