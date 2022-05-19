'''The user enters a cost and then the amount of money given.
The program figures out the change and the number of quarters, dimes, nickels, pennies needed for the change.'''
import ask_usr

# cost = 10.58 # dollars
# given = 11 # dollars

cost = ask_usr.ask_usr_num(option='the cost of the article: ')
given = ask_usr.ask_usr_num(option='the money given: ')

txt = 'You must return '
coin_names = ['dollar', 'quarter', 'dime', 'nickel', 'penny']
coin_values = [1, 0.25, 0.10, 0.05, 0.01]

change = round(given - cost, 2)
if change < 0:
    print('You have not enough money.')
elif change == 0:
    print('No change left')
else:
    print('The change is: ', change)
    for coin_name, coin_value in zip(coin_names, coin_values):
        if change / coin_value < 1:
            # For this case, you have not even 1 "coin_value" to return
            continue
        elif change / coin_value == 1:
            num_coins = int(change / coin_value)
            if txt == 'You must return ':
                txt += str(f"{num_coins} {coin_name} ")
            else:
                txt += str(f"and {num_coins} {coin_name} ")
            break  # You found the smallest coin you can return according to the change
        elif change / coin_value > 1:
            num_coins = int(change / coin_value)
            if coin_name == 'penny':
                if txt == 'You must return ':
                    txt += str(f"{num_coins} {coin_name}")
                else:
                    txt += str(f"and {num_coins} {coin_name}")
            else:
                txt += str(f"{num_coins} {coin_name}")
            if num_coins == 1:
                txt += ', '
            elif num_coins > 1:
                if coin_name == 'penny':
                    txt = txt[:-1]
                    txt += 'ies '
                else:
                    txt += 's, '
            change = round(change - coin_value * num_coins, 2)  # The remaining is the new change
            continue

    if txt.endswith(', '):
        txt = txt[:-2]

    print(txt)