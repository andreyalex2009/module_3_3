def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [2, 'Привет', False]
value_dict = {'a': 3, 'b': 'Пока', 'c': 5.6}

print_params(*values_list)
print_params(**value_dict)

values_list_2 = [3, 'Жора']

print_params(*values_list_2, 42)