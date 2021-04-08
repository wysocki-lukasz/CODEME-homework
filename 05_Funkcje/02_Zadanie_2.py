# coding=utf-8
# 2▹ Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

def minimum_of(a,b,c):
    if a < b and a < c:
        result = a
    elif b < a and b < c:
        result = b
    elif c < a and c < b:
        result = c
    return result

print(minimum_of(3,5,1))