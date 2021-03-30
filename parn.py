

from collections import deque

def balanced_paran(sr):
	k=deque()
	for i in sr:
		if i=='[' or i=='{' or i=='(':
			k.append(i)
		elif i==')' :
			if len(k)==0:
				return 'Unbalanced'
			elif k[-1]=='(':
				k.pop()
		elif i==']':
			if len(k)==0:
				return 'Unbalanced'
			elif k[-1]=="[":
				k.pop()

		elif i=='}':
			if len(k)==0:
				return 'Unbalanced'
			elif k[-1]=='{':
				k.pop()
		else:
			return 'Unbalanced'
	if len(k)==0:
		return 'Balanced'

st=input('Enter parantheeses')

print(balanced_paran(st))