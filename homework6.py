my_dict = {'Sasha': 1999, 'Oleg': 1957, 'Marusya': 1978}
print(my_dict)
print(my_dict['Oleg'])
print(my_dict.get('Ivan'))
my_dict.update({'Elena': 1982, 'Egor': 2000})
print(my_dict)
my_dict.pop('Sasha')
print(my_dict)

my_set = {2, 5, 8, 5, 2, 'ball', 'roll', 'ball', (8, 7, 6)}
print(my_set)
my_set.add(('pasta', 'pizza'))
my_set.add(9)
print(my_set)
my_set.discard((8, 7, 6))
print(my_set)