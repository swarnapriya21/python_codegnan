'''d={1:"A","A":1,"hi":"hello",(1,2,3):(10,20,30),12.241:10.00}
print(d)

#duplicate keys
d={1:"A","A":1,"hi":"hello",(1,2,3):(10,20,30),12.241:10.00,1:'z'}
print(d)

#values access by passing keys
d={1:"A","A":1,"hi":"hello",(1,2,3):(10,20,30),12.241:10.00,1:'z'}
print(d[1])
print(d["A"])
#update values and items
d[1]="x"
print(d[1])
d['1']='x'
print(d['1'])
print(d)

#empty dictionary representation
d1={}
d2=dict()
print(type(d1),type(d2))'''

###Methods
'''-get(key,default)-it returns the values if present in dictionary,otherwise deafault value
-updte(new-dict)-it updates the dictionary with new-dictionary items
-pop(key)-it return and removes the item,if key is present in dictionary otherwise last key error
-
-keys()-it returns the list of keys 
-values()-it returns the list values 
-items()-it returns the list of tuple of key value pairs
-clear()-it removes all items from the dictionary'''

'''#update
d1={"batch":39,'course':"pfs"}
d2={'course':"jfs","lang":"java"}
d1.update(d2)
print(d1)'''

#popitems(),clear()
d={'batch':39,'course':'pfs','lang':'python'}
print(d.popitems())
print(d.pop('cour
