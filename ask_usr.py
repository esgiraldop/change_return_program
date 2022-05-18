def check_num(num):
    '''Function to check no weird values are given by the user'''
    # Check that numbers with no more than 2 decimals are given
    # Check that no negative numbers are given
    pass

def ask_usr_num(option):
    num = '1'
    while type(num) != type(1) and type(num) != type(1.0):
        num = input('Please enter '+option).lower()
        opt = any([num == 'inf', num == '-inf', num == 'nan', num == '-nan'])
        if opt:
            print('Please input a valid answer')
            num = str(num)
            continue
        try:
            num = float(num)
        except:
            if type(num) != type(1) and type(num) != type(1.0):
                print('Please input a valid answer')
        else:
            return num

if __name__ == '__main__':
    num = ask_usr_num()
    print('The number is: ', num)