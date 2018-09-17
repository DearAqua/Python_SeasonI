#   import
import calendar

#   input
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

#   deal
monthRange = calendar.monthrange(yy,mm)

#   ouput
print(monthRange)

#   Special deal
if int(monthRange[0]) == 0:
    print('星期一')
elif int(monthRange[0]) == 1:
    print('星期二')
elif int(monthRange[0]) == 2:
    print('星期三')
elif int(monthRange[0]) == 3:
    print('星期四')
elif int(monthRange[0]) == 4:
    print('星期五')
elif int(monthRange[0]) == 5:
    print('星期六')
else:
    print('星期天')

