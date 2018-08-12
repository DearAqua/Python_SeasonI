dict1 = { 'title': 'General' };
dict2 = { 'title': 'Viceroy', 'name': 'Vittorio','age': 3,'ability': 100 };
 
print ("dict2['Name']: ", dict2['name'])
print ("dict2['Age']: ", dict2['age'])

print ('3 years latter')

# 更新 Age
dict2['age'] = 6;
# 添加信息
dict2['family'] = "Italy"
 
print ("dict['Age']: ", dict2['age'])
print ("dict['Family']: ", dict2['family'])

'''
del dict2['family']
print(dict2)
dict1.clear()
print(dict1)
del dict1
print(dict1)
'''



