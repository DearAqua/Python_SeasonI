#   不重复特性
orchestra = {'violin', 'brass', 'brass', 'woodwind', 'Percussion'}
print(orchestra)
#   判断元素
print('woodwind' in orchestra)                 
print('shotgun' in orchestra)
#   添加元素
orchestra.add('violin')
orchestra.add('pistol')
print(orchestra)
print('=========================')
#   移除元素
orchestra.remove('pistol')
print(orchestra)
orchestra.discard('shotgun')
print(orchestra)
print('=========================')
#   特殊玩法
print(orchestra.pop())
print(orchestra)
#   清空集合
orchestra.clear()
print(orchestra)
print('=========================')

a = set('Viceroy')
b = set('Vittorio.Veneto')
print(len(a))
print(len(b))
print(a)                                  
# 集合a中包含元素
print(a-b)
# 集合a或b中包含的所有元素
print(a|b)
# 集合a和b中都包含了的元素
print(a&b)
# 不同时包含于a和b的元素
print(a^b)

