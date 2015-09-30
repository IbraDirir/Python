a = ['spam', 'eggs', 100, 1234]
print (a)
a[2] = a[2] + 23
print (a)
a[0:2] = [1, 12]
print(a)
a[0:2] = []
print(a)
a[1:2] =  ['bletch', 'xyzzy']
print (a)
a[:0] = a
print(a)
