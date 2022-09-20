""". Write a python program to change the first item (22) of a list within the following tuple to 222.
tuple1 = (11, [22, 33], 44, 55)"""
tuple1 = (11, [22, 33], 44, 55)
List = list(tuple1)
List[1] = 222
tuple1 = tuple(List)
print(tuple1)
"""""""""""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""""""""""""""""""
"""
(11, 222, 44, 55)
"""