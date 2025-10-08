#t=(1,2,3,[10,20,30],"codegnan")
#print(t)

#t=tuple(map(int,input().split()))
#print(t)

'''t=(1,2,3,[10,20,30],"codegnan")
print(t[2],t[-2],t[-4])
print(t[-1:2:-1])
print(t[3:-4:-1])'''
'''#single element representation in tuple
t=(29)
t2=(20)
print(type(t), type(t2))'''

#tuple operations
#concatanation operation
'''t1=(1,2,3)
t2=('A',"b")
t3=t1+t2
print(t3)'''

'''#tuple operations
#repetation operations
t1=(1,2,3)
t=t1*3
print(t)'''

'''t=(1,2,3,[10,20,30],"codegnan")
ind=t.index(3)
count=t.count(3)
print(ind,count)'''

'''#built in function
#Len(),min(),max(),sum()
t=(1,2,3,4,5)
print(len(t),min(t),max(t),sum(t))'''

#string to tuple cenversation
s="codegnan"
print(list(s))
print(tuple(s))
#tuple to list conversation
t=(1,2,3,4,5)
print(list(t))
