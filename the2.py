# Program to check the validity of a METU student ID number
# Written in 2015
# by Sena Temuçin



number = raw_input("Input?")
i = number.find('?')
number = list(number)
if i==7:
	number[7]=str((10-(int(number[0]) + int(number[2]) + int(number[4]) + (int(number[1])*2)%10+(int(number[1])*2)/10 + (int(number[3])*2)%10+(int(number[3])*2)/10 + (int(number[5])*2)%10+(int(number[5])*2)/10)%10)%10)
	new = "".join(number)
	print new
elif i==-1:
	if (int(number[0]) + int(number[2]) + int(number[4]) + (int(number[1])*2)%10+(int(number[1])*2)/10 + (int(number[3])*2)%10+(int(number[3])*2)/10 + (int(number[5])*2)%10+(int(number[5])*2)/10 + int(number[7]))%10==0:
		print 'VALID'
	else:
		print 'INVALID'
elif i==0:
	number[0]=str((10-(int(number[7]) + int(number[2]) + int(number[4]) + (int(number[1])*2)%10+(int(number[1])*2)/10 + (int(number[3])*2)%10+(int(number[3])*2)/10 + (int(number[5])*2)%10+(int(number[5])*2)/10)%10)%10)
	new = "".join(number)
	print new
elif i==2:
	number[2]=str((10-(int(number[7]) + int(number[0]) + int(number[4]) + (int(number[1])*2)%10+(int(number[1])*2)/10 + (int(number[3])*2)%10+(int(number[3])*2)/10 + (int(number[5])*2)%10+(int(number[5])*2)/10)%10)%10)
	new = "".join(number)
	print new
elif i==4:
	number[4]=str((10-(int(number[7]) + int(number[0]) + int(number[2]) + (int(number[1])*2)%10+(int(number[1])*2)/10 + (int(number[3])*2)%10+(int(number[3])*2)/10 + (int(number[5])*2)%10+(int(number[5])*2)/10)%10)%10)
	new = "".join(number)
	print new
elif i==1:
	remainder=((10-(int(number[7]) + int(number[0]) + int(number[2]) + int(number[4]) + (int(number[3])*2)%10+(int(number[3])*2)/10 + (int(number[5])*2)%10+(int(number[5])*2)/10)%10))%10
	if remainder%2==0:
		number[1]=str(remainder/2)
	else:
		number[1]=str((remainder+9)/2)
	new = "".join(number)
	print new
elif i==3:
	remainder=((10-(int(number[7]) + int(number[0]) + int(number[2]) + int(number[4]) + (int(number[1])*2)%10+(int(number[1])*2)/10 + (int(number[5])*2)%10+(int(number[5])*2)/10)%10))%10
	if remainder%2==0:
		number[3]=str(remainder/2)
	else:
		number[3]=str((remainder+9)/2)
	new = "".join(number)
	print new
elif i==5:
	remainder=((10-(int(number[7]) + int(number[0]) + int(number[2]) + int(number[4]) + (int(number[3])*2)%10+(int(number[3])*2)/10 + (int(number[1])*2)%10+(int(number[1])*2)/10)%10))%10
	if remainder%2==0:
		number[5]=str(remainder/2)
	else:
		number[5]=str((remainder+9)/2)
	new = "".join(number)
	print new