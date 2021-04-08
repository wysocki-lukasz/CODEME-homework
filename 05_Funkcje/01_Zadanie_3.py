# coding=utf-8
# 3▹ Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def sum(numbers):
    init_sum = 0
    for number in numbers:
        init_sum += number

    return init_sum


result = sum([1,2])
print(result)
