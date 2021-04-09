# coding=utf-8
# 6▹ Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

#All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#American Express card numbers start with 34 or 37 and have 15 digits.

def card_reader(file):
    with open(file, 'r') as fopen:
        lines = fopen.readlines()
    return lines

def visa_check(card_num):
    if card_num[0] == '4' and len(card_num) in [13,16]:
        card_type = 'Visa'
    return card_type


def mastercard_check(card_num):
    if (int(card_num[0:2]) in [51,55,1] or int(card_num[0:5]) in [2221,2720,1]) and len(card_num)==16 :
        return True
    else:
        return False

def amex_check(card_num):
    if card_num[0:2] in ['34', '37'] and len(card_num)==15:

        return True
    else:
        return False

def save_cards_number(filename, card_type,card_num):
    with open(filename, 'a') as fp:
        fp.write(card_type + card_num + '\n')


file = 'karty_kredytowe.txt'
print (card_reader(file))

for card_num in card_reader(file):
    card_num = card_num.replace(' ','').strip()
    print (card_num)
    if card_num is visa_check(card_num):
        print('Visa card')


    elif card_num is mastercard_check(card_num):
        print('Mastercard')
        card_type = 'Mastercard'
    elif card_num is amex_check(card_num):
        print('AmericanExpress')
        card_type = 'AmericanExpress'

save_cards_number('typ_karty_kredytowe.txt', card_type ,card_num)

