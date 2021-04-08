# coding=utf-8
## 4▹ Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def sum(numbers):
    init_sum = 0
    for number in numbers:
        if number%2 ==0:
            init_sum += number

    return init_sum


result = sum([1,2,4,5,7,9])
print(result)
