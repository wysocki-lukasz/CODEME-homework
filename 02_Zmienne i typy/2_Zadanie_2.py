# !!Pomylka w ozaczeniu nazwy - winno byc 1_Zadanie_2.py
# Dla podanej liczby w systemie dwójkowym bin_num = 1001111 oblicz wartość w systemie dziesiętnym.
# Zamianę z systemu binarnego na dziesiętny napisz samodzielnie (nie korzystaj z metody wbudowanej).

bin_num = 1001111

conv_bin_num = 1*2**6 + 0*2**5 + 0*2**4 + 1*2**3 + 1*2**2 + 1*2**1 + 1*2**0
print(f'Liczba binarna {bin_num} w systemie dziesietym to {conv_bin_num}.')