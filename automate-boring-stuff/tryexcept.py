def division(a,b):
	try:
		return a/b
	except:
		print('some error occured')#no return

print(division(1,2))
print(division(2,0))
print(division('a',3))

def compareNum(a,b):
	try:
		return max(a,b)
	except:
		print('error')

print(compareNum(1,2))
print(compareNum('a','b'))
print(compareNum('a',1))