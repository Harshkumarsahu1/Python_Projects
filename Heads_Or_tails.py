import random
h = "Heads"
t = "Tails"
random_number = random.uniform(0, 1)
if random_number < 0.5:
    print(h)
else:
    print(t)