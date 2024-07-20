my_dict = {'Dima' : 1994, 'Anton' : 1995, 'Vladimir' : 1967, 'Elena' : 1970}
print(my_dict)
print(my_dict['Elena'])
my_dict['Andrey'] = 1989
print(my_dict)
my_dict.update({'Boris': 1992, 'Alex': 1990})
print(my_dict)
del my_dict['Boris']
print(my_dict)

my_set = {1998, 1999, 2000, 2001, 2000, 1999, (20,19,18), "satelit", False}
print(my_set)
print(my_set.add(1997))
print(my_set.add(1996))
print(my_set)
print(my_set.discard(1996))
print(my_set.remove(1997))
print(my_set)
