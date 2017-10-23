while True:

    in_value = input('please give a number : ')

    if in_value < 10:
        print('input-value is lower')
        break

    if in_value > 10:
        print('input-value is bigger than 10')
    elif in_value == 10:
        print('input-value is equals to 10')

print('exit.')
