'''
data = 'I will be in a file.\nSo cool!'
targetfile  = open('..\Py-data\#023.txt','w')
targetfile.write(data)
targetfile.close()
'''
data = '来试试追加模式'
targetfile  = open('..\Py-data\#023.txt','a')
targetfile.write(data)
targetfile.close()
