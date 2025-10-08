'''s={1,2,34,20.25,"codegnan",(1,2,3),1,2}
print(s)

#empty set creation
s1={}
s2=set()
print(type(s1),type(s2))'''

'''#read set of integered from user
s=set(map(int,input().split()))
print(s)'''


'''#set operations
s1={1,2,"hi","hello"}
s2={"python",'java'}
print("union:",s1.union(s1))
print("intersection:",s1.intersection(s2))
print("defference:",s1.intersection(s2))
print("symmetric difference:",s1.symmetric_difference(s2))
print("subset:",s1.issubset(s2))
print("superset:",s1.issuperset(s2))
print("dis joint set:",s1.isdisjoint(s2))'''


'''#set operations
s1={1,2,5}
s2={1,3,4,5}
print('''

s={1,2,3,5,65,43}
s1.add(100)
s1.add(1)
print(s1)
s1.remove(100)
print(s1)
s1.discard(100)
s1.discard(2)
print(s1)
s1.update({1,2,3})
print(s1)

