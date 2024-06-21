# total=0
# for i in range(1,101):
#   total+=i
# print(total)
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!9
print("Your password :-",end="")
for alphabets in range(1,nr_letters+1):
  random_letters=random.choice(letters)
  print(random_letters,end="")
for symbol in range(1,nr_symbols+1):
  random_symbols=random.choice(symbols)
  print(random_symbols,end="")
for number in range(1,nr_numbers+1):
  random_numbers=random.choice(numbers)
  print(random_numbers,end="")

print("\n")
password=[]
for char in range(1,nr_letters+1):
  password.append(random.choice(letters))
for char in range(1,nr_symbols+1):
  password.append(random.choice(symbols))
for char in range(1,nr_numbers+1):
  password.append(random.choice(numbers))
# print(password)
random.shuffle(password)
print("Your second password is:- ","".join(password))
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8


# creating a password based on the specific length
password_len=int(input("Enter the length of the password:- "))
passkey= " "
for char in range(1,password_len+1):
  passkey+=random.choice(letters)
for char in range(1,password_len+1):
  passkey+=random.choice(symbols)
for char in range(1,password_len+1):
  passkey+=random.choice(numbers)
print(passkey)