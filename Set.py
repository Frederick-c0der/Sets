numbers={1,9,2,4,5,7,3,8,6} #Sets are unique un repeated collections not ordered
print(numbers)
numbers.add(10)#add something to set
print(numbers)
numbers.remove(3)#remove something from set
print(numbers)
numbers.add(10)#Even though there is 2 10s it shows only once
print(numbers)
print(len(numbers))#length of set
length=len(numbers)
for i in numbers:#prints set one by one(works for every data structure except dictionary)
    print(i)
set1={24,1,4,24,465,212,35,2,3,2,1,234}
set2={354,32,12,212,454,456,1233,356}
print(set1.union(set2))#combines sets
print(set1.intersection(set2))#common elements of each set
print(set1.difference(set2))#common elements removed from set1
print(set2.difference(set1))#common elements removed from set2
print(set1.symmetric_difference(set2))#everything but duplicate items
set3={4,6,8}
set4={4}
print(set4.issubset(set3))#if one set's elements are in another's set
print(set3.issuperset(set4))