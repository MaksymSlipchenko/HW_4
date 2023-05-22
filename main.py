#1 Tuple
tuple = (1, 2, 3, 4, 5, 6, 7)
print(tuple)

#2 Set
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {5, 6, 7, 8, 9, 10, 11}
set1.add(0)
set3 = set1.intersection(set2)
print(set3)
set4 = set1.difference(set2)
print(set4)
set5 = set1.symmetric_difference(set2)
print(set5)