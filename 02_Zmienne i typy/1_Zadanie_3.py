# Dla liczb hex_num = 1DB i oct_num = 2063 zwróć wartość w systemie dziesiętynym
hex_num = '1DB'
oct_num = '2063'

conv_hex_num = int(hex_num,16)
conv_oct_num = int(oct_num,8)

print(f'W systemie dziesietnym, liczba {hex_num} to liczba {conv_hex_num} .')
print(f'W systemie dziesietnym, liczba {oct_num} to liczba {conv_oct_num} .')