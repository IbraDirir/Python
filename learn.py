#for loop
a =  ['cat', 'cow', 'camel', 'sheep']
for  x in a:
    print(x, len(x))
for  x in a[:]:
    if len(x) > 6: a.insert(0 , x)
    print(a)