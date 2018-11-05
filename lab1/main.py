class RangeException(Exception):
	pass
try:
 num = int(input('Enter number\n'))
 if ((num<0) or (num>9)):
  	raise RangeException('This number no in range')
except RangeException:
	print('This number no in range, repeat please')
	num = int(input('Enter number\n'))
except ValueError:
	print('The character entered is not a number, reapead please')
num = int(input('Enter number'))
ans = input('push ="yes", if you want to transfer this number to any number system, or "no", if you want to see only the name of the number you entered - ')
if (answer == 'yes'):
	typ = input('"bin"-binary system\n"oct"-octal system\n"hex"-hexadecimal system\n')
else:
	typ=''

if (num == 0):
	print('Zero')
elif (num == 1):
    print('One')
elif (num == 2):
    print('Two')
elif (num == 3):
    print('Free')
elif (num == 4):
    print('Four')
elif (num == 5):
    print('Five')
elif (num == 6):
    print('Six')
elif (num == 7):
    print('Seven')
elif (num == 8):
    print('Eight')
elif (num == 9):
    print('Nine')
'''else:
	print('This number no in range')'''
	

sys_of_num = str(input('select systen of number\n'))

if (sys_of_num == 'bin'):
	print(bin(num))
elif (sys_of_num == 'oct'):
	print(oct(num))
elif (sys_of_num == 'hex'):
	print(hex(num))

	#assert func(0,'') == 'ноль', 'Название цифры не верно'
	#assert func(1,'oct') == '0o1', 'Название или перевод цифры не верен'
	#assert func(3,'hex') == '0x3', 'Название или перевод цифры не верен'


