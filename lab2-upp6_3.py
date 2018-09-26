# Stars - ett program av ...
def triangel_bas_ned(a,b):
	i=0
	s=''
	while b-2*i > 0:
		s=s+((int(b/2)-i+a)*' '+(2*i+1)*'*'+'\n')
		i += 1
	return s;
def triangel_bas_upp(a,b):
	i=0
	s=''
	while b-i *2> 0:
		s=s+((i+a)*' '+(b-i*2)*'*'+'\n')
		i += 1
	return s;
def romb(a,b):
	s=	triangel_bas_ned(a,b)+triangel_bas_upp(a+1,b-2)
	return s;
print (romb(3,11))
input ("\nPress Enter to exit")