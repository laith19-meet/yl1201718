## problem 1
list1=[1,3,5,7,9]
list2=[]
list2.append(list1[0])
list2.append(list1[-1])
print list2

##problem 2 A

list3 = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(list3)):
	if list3[i] < 5 :
		print list3[i]

##problem 3
list0 =[1,2,3,4,5,6,7,8,9]
listt = [1,3,5,7,9,77,55,35,24]
def mostcommon(list0,listt):
	result = []
	for value in list0:
		if value in listt:
			result.append(value)


##problem 4

n = input("answer : ")

for x in range(2,n):
	if n%x == 0 
		print ("not prime")
	elif: 
		print ("prime")

	
