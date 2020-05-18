#!/usr/bin/python3

# Vivi-注释

# 第一个注释
# 第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""

# Vivi-输出

print ("Hello, Python!")

x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()


# Vivi-缩进


if True:
    print ("True")
else:
    print ("False")

# Vivi-多行

total = 1 + \
        2 + \
        3
print(total)

# Vivi-字符串

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

print(word)
print(sentence)
print(paragraph)

str='QuickStart'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nViceroy')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello \n Viceroy')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
