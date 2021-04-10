# 1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp. W pętli spróbuj
# wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

element = [13, 'string', 2.45, 0]
collected_errors = []

for i in element:
    try:
        result = 10 / i
    except TypeError as e:
        result = 0
        collected_errors.append(e)
    except ZeroDivisionError as e:
        result = 1
        collected_errors.append(e)

    print(result)

for err in collected_errors:
    print(f'- {err}')