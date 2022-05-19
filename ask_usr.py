def ask_usr_num(option):
    '''Function for asking a number to the user and then checking it is not a weird value.'''
    while True:
        num = input('Please enter '+option).lower()
        opt = any([num == 'inf', num == '-inf', num == 'nan', num == '-nan'])

        if opt:
            # Checking that inf or nan values are given
            print(f'{num} is not a valid answer')
            continue

        try:
            # Checking that only numbers are given
            num = float(num)
        except:
            print('Please input a number.')
            continue
        else:
            if '.' in str(num):
                float_part = str(num).split('.')[1]
            else:
                float_part = '0'

            if len(float_part) > 2:
                # Checking that numbers with no more than 2 decimals are given
                print('Do not input numbers with more than 2 decimals.')
                continue
            elif num < 0:
                # Checking that no negative numbers are given
                print('Do not input negative numbers.')
                continue
        break
    return num

if __name__ == '__main__':
    option = 'the cost of the article: '
    num = ask_usr_num(option)
    print('The number is: ', num)