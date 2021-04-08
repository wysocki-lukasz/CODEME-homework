# coding=utf-8
# 3▹ Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def maximum_of(a,b,c):
    if a > b and a > c:
        result = a
    elif b > a and b > c:
        result = b
    elif c > a and c > b:
        result = c
    return result

print(maximum_of(3,5,1))