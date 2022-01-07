import random


def coinflip():
    result = []
    streak = 0
    count = 0
       # This part flips the coin 100 times and stores it in a list
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            result.append('H')
        else:
            result.append('T')

    # This part counts the amount of times that there is a streak.
    for j in range(len(result)):
        if j == 0:
            previous = result[j]
        
        elif result[j] == result[j-1]:
            count += 1
            
            if count == 6:
                streak += 1
        else:
            count = 0
    print(streak)
coinflip()
