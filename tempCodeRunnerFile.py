import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '+', '=', '[', ']',
    '{', '}', '|', ';'
]

n_letters = int(input("Enter The Number Of Letters Do You Want In Your Password :"))
n_num = int(input("How Many Numbers You Want In Your Password :"))
n_symbols = int(input("Enter The Number Of Symbols Do You Want In Your Password :"))

password = ""
for i in range(n_letters):
    char = random.choice(letters)
    password = password+char 

for i in range(n_num):
    char = random.choice(numbers)
    password = password+char 

for i in range(n_symbols):
    char = random.choice(symbols)
    password = password+char 

password = list(password)
random.shuffle(password)
password = "".join(password)
print(password)
    