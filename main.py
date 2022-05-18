cost = 10.58 # dollars
given = 11 # dollars
txt = 'You must return '
coin_names = ['dollar', 'quarter', 'dime', 'nickel', 'penny']
coin_values = [1, 0.25, 0.10, 0.05, 0.01]

change = round(given - cost, 2)
print('The change is: ', change)

if change < 0:
    print('You have not enough money.')
elif change == 0:
    txt = 'No change left'
else:
    for coin_name, coin_value in zip(coin_names, coin_values):
        if change / coin_value < 1:
            # For this case, you have not even 1 "coin_value" to return
            continue
        elif change / coin_value == 1:
            txt += str(f"and {coin_value} {coin_name} ")
            break  # You found the smallest coin you can return according to the change
        elif change / coin_value > 1:
            num_coins = int(change / coin_value)
            if coin_name == 'penny':
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

print(txt)