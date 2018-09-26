# Stars - ett program av ...
def triangel_bas_upp(a,b):
	i=0
	s=''
	while b-i *2> 0:
		s=s+((i+a)*' '+(b-i*2)*'*'+'\n')
		i += 1
	return s;
print (triangel_bas_upp(3,11))
input ("\nPress Enter to exit")