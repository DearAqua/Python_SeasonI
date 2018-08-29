def sayHello():
    print('hello world!')

def area(width, height):
    return width * height

sayHello()

print('计算矩形面积')
print('高')
h = int(input())
print('宽')
w = int(input())

print( "area =", area(w, h))
