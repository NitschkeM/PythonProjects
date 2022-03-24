# State as Clearly as Possible What we want to happen.
# State Intent as Clearly as Possible.
# If I wish to do so and if it feels appropriate - Feel Free to Visualize what it would Look Like and Imagine what it would Feel Like


### That it Feels Peaceful to: ###
# Read Input From File
# Read Numbers from day_1-input_1.txt into a List in a Python Program

import random

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))

# print(bernoulli_trial(50))
print(binomial(1000, 0.5))

# for i in range(5):
#     print(random.random())