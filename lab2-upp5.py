# Stars - ett program av ...
def triangel_bas_ned(a,b):
	i=0
	while b-2*i > 0:
		print((int(b/2)-i+a)*' '+(2*i+1)*'*')
		i += 1
def triangel_bas_upp(a,b):
	i=0
	while b-i *2> 0:
		print((i+a)*' '+(b-i*2)*'*')
		i += 1
def romb(a,b):
	triangel_bas_ned(a,b)
	triangel_bas_upp(a+1,b-2)
romb(2,9)
input ("\nPress Enter to exit")