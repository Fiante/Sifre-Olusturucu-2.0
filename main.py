import string
from random import sample

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
total = letters + digits + punctuation

length = int(input("Uzunluk: "))

password = "".join(sample(total, length))

print("Şifreniz:", password)
