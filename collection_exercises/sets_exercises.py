#sets:unorders,unchangeable, no duplicalte values

set1= {1,2,3,4,5}
print(type(set1))
print(len(set1))
print(set1)

#add new item
set1.add(6)
print(set1)

fruit_set={'bnana','apple','orange','kiwi'}
set1.update(fruit_set)
print(set1)

#remove
set1.remove('bnana')
print(set1)
"""
set1.remove('grape')
print(f"remove results:{set1}")
"""


#discard
set1.discard('grape')
print(f"discard result:{set1}")

#pop
set1.pop()
print(set1)


set1.clear()
print(set1)

del set1
print(set1)