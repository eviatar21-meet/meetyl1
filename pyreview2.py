def common_numbers(list1,list2):
	commonList=[]
	for number in list1:
		if number in list2:
			commonList.append(number)
	return commonList
b=input("write numbers")
c=input("write numbers")
a=common_numbers(b,c)
print(a)
