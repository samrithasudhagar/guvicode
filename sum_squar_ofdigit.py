n=int(input())
s=0
while n>0:
	r=n%10
	s=s+(r*r)
	n=n//10
print(s)
#...sum of squares of digit..
