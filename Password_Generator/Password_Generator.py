import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '&', '*', '=', '+',]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Welcome to the Password Generator!")
nr_letters = int(input("How Many Letters Would You in Your Password : \n"))
nr_symbols = int(input("How Many Symbols Would You in Your Password : \n"))
nr_numbers = int(input("How Many Numbers Would You in Your Password : \n"))

Password_list = [ ]

for char in range (0, nr_letters):
    Password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    Password_list.append(random.choice(symbols))

for char in range (0, nr_numbers):
    Password_list.append(random.choice(numbers))

print(Password_list)
random.shuffle(Password_list)
print(Password_list)

Password = ""

for char in Password_list: 
    Password += str (char)
print(f"Your Password is : {Password}")

