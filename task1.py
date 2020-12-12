#get 20 random integers
def random(min=1, max=6, count=1, seed=None):
    import random
    random.seed(seed)
    return tuple([random.randint(min, max) for i in range(0, count)])

def median_odd(numbers):
    index = len(numbers) // 2
    return sorted(numbers, reverse=True)[index - 1]

def median_even(numbers):
    index = None
    if len(numbers) % 2 == 0:
        #if even
        index = int(len(numbers) / 2)
        high = sorted(numbers, reverse=True)[index - 1]
        low = sorted(numbers, reverse=True)[index]
        return (high + low) / 2
    else:
       #if odd 
        return median_odd(numbers)

def mode(numbers):
    frequency = {x : numbers.count(x) for x in set(numbers)}
    result = tuple([key for key, val in frequency.items() if val == max(frequency.values())])
    if len(result) == 1:
        return result[0]
    return result

def main(test=False):
    MIN = 100
    MAX = 120
    COUNT = 20
    SEED = 2020
    if test:
        COUNT = COUNT * 10 
        COUNT += 1 
        SEED = None 

    rand = random(MIN, MAX, COUNT, SEED)
    print(f'rand: {rand}')
    print(f'median: {median_even(rand)}')
    print(f'mode: {mode(rand)}') 

    if test:
        print(f'min(rand) == {MIN}? {min(rand) == MIN}') 
        print(f'max(rand) == {MAX}? {max(rand) == MAX}') 

main(0) 