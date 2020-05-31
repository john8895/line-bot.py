import random


store_data = ['龍品魚丸', '原食', '濰克']

num = random.randint(0, len(store_data)-1)


if '吃什麼' in msg:

print(store_data[num])