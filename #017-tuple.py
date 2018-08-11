tup1 = ('Viceroy', 'Vittorio','Veneto', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
print(type(tup1))
tup2 = ();
print(type(tup2))
tup2 = (1)
print(type(tup2))
tup2 = (1,)
print(type(tup2))

print('====================')

tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print ("tup1[0:3]: ", tup1[0:3])
print ("tup2[1:5]: ", tup2[1:5])

print(tup1[2])
print(tup1[-2])
print(tup1[1:])      

print('====================')

tupop = ('td',)
tupcl = ('/td',)
tupcontent = ('content',)

tuphtml = tupop + tupcontent + tupcl
print(tuphtml)

print(tup2 * 4)
print('Viceroy' in tup1)
for x in tup1:
    print(x,)

print(len(tup1))
print(max(tup2))
print(min(tup2))
list1 = ['this','is','the','list']
print(list1)
tuple1 = tuple(list1)
print(tuple1)

del tuple1
print (tuple1)

