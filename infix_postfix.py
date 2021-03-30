from collections import deque


def inf_to_postf(expression):
	stack=deque()
	result=''

	for i in expression:

		if i=='(' or i in ['+','-','*','/'] :
			stack.append(i)
		elif i.isalpha():

			result+=i

		elif i== ')':
			j=''
			while j !='(':
				j=stack.pop()
				if j!='(':
					result+=j

	return result

ex='((A+b)*(C-D))'

print (inf_to_postf(ex))