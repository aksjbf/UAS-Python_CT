import random, string
print('Selamat datang di Password Generator')

char1 = 'abcdefghijklmnopqrstuvwxyz'
cap = char1.upper()
symbol = string.punctuation

chars = char1 + cap + symbol
print(chars)

number = int(input('Total password yang ingin generate : '))
length = int(input('Input berapa panjang karakter password kamu : '))

print('\n Ini hasil password mu : ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
