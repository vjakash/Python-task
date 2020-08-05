tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']] 
result=[];
for i in range(len(tableData[0])):
	for j in range(len(tableData)):
		result.append(tableData[j][i])
	print(*result)
	result=[]
#prob-2
lookup={'i':1,'v':5,'x':10}
def transform(romanNum):
  num=0;
  i=0;
  while i<len(romanNum):
    str1=romanNum[i]
    if i+1 < len(romanNum):
      str2=romanNum[i+1]
      print(str1,str2)
      if lookup[str1]>=lookup[str2]:
        num=num+lookup[str1]
        i+=1
      else:
        num=num+lookup[str2]-lookup[str1]
        i+=2
    else:
      num+=lookup[str1]
      i+=1
  return num
result=transform('xiv')
print(result)

#prob-3
inp=int(input('enter a number:'))
if inp>0 and inp<13:
	if inp==2:
		print(28)
	elif inp%2==0 and inp<=7:
		print(30)
	elif inp%2!=0 and inp<=7:
		print(31)
	elif inp%2==0 and inp>7:
		print(31)
	else:
		print(30)
else:
	print('invalid number')

#prob-4
def transform(list):
  if len(list)<2:
    return (''.join(list))
  temp=', '.join(list[0:-1:])
  return (',and '.join([temp,list[-1]]))
result=transform( ['apples', 'bananas', 'tofu', 'soya'] )
print(result)
