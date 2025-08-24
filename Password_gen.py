import random
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
latters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z"]
n_number = int(input("How many numbers do you want in your password? "))
n_symbol = int(input("How many symbols do you want in your password? "))
n_latter = int(input("How many latters do you want in your password? "))

password = []
for i in range(n_number):
    password.append(random.choice(number))
for i in range(n_symbol):
    password.append(random.choice(symbol))       
for i in range(n_latter):
    password.append(random.choice(latters))

random.shuffle(password)  # Shuffle the password list to mix numbers, symbols, and letters
password = ''.join(password)  # Join the list into a string
print("Your password is: " + password)