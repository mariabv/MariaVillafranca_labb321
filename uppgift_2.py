def is_number_try(s):
    """ Returns True if string is an integer. """
    try:
        int(s)
        return True
    except ValueError:
        return False
print('This program asks you to type two digital numbers and returns summa of their cubes\n\nSo, let\'s start...\n')
a = input('Input a =  ')
b = input('Input b =  ')
if is_number_try(a) and is_number_try(a):
	a=int(a)
	b=int(b)
	print 'Result is ',a**3+b**3
else:
	print('Sorry, I can calculate only for integers.\n')
input('Press ENTER to exit, please')
