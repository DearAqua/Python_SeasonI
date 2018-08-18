file  = open('..\Py-data\#024.txt')
lines = file.readlines()
print(lines)
file.close()

results = []   

for line in lines:
   #print(line)
   data = line.split()
   #print(data)

   sum = 0
   for score in data[1:]:
       sum += int(score)
       #print(sum)
   result = '%s \t: %d\n' % (data[0], sum)
   #print(result)

   results.append(result)
   #print(results)

targetfile  = open('..\Py-data\#024-output.txt','w')
targetfile.writelines(results)
targetfile.close()
