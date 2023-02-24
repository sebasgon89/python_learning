import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
pw_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
pw_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

password_aux = pw_symbols + pw_letters + pw_symbols
random.shuffle(password_aux)

password = "" . join(password_aux)

print(password)
pyperclip.copy(password)