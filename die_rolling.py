#simulating a die until it turns 5

import random
min = 1
max = 6

roll_again = True

while roll_again:
    print('Rolling the dices...')
    result = random.randint(min,max)
    print(result)

    break

roll_again = False
repeater = input('Do you want to roll again :')
