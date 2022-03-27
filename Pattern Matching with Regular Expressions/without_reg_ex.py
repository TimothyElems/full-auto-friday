'''
all good programmers start with documentation

This first program is showing how to find patterns without usign Regular Expressions. A sort of before and after approach to the thingy.
'''
print('I\'m too segsy for my shirt.')
def isPhoneNumber(text):
	if len(text) != 12:
		return False 
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text [7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True
	
print('269-471-6818 is a phone number:')
print(isPhoneNumber('269-471-6818'))
print('Yama yama is a phone number:')
print(isPhoneNumber('Yama yama'))
