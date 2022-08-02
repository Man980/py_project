#Don't forget to put in comment the other exercices when executing 

#Exercice 1
'''
#ip = input("Enter you IP address\n>>> ")
ip =input('Enter your IP address. egz: 192.168.192')
ip = ip.replace('.','')

first_letter = int(ip[0])
add =0
for x in ip:
	add +=int(x)
print(add*first_letter)
'''
'''
#Exercice 2
#As it is so simple, it is something made for beginners in a challenge

integer= int(input('Enter an enteger:\n>>> '))
if integer % 4 != 0:
	print('OK')
else:
	print('NOK')

'''
'''
#Exercice 3

name = input("Enter your name:\n>>> ")

new_name = ''
for x in name.lower().split():
	new_name+=x.capitalize()+' '
print(new_name)
'''

#Exercice 4
a = 2
b = 3
number =[2, 4, 5, 8, 9, 12, 15, 18]

ad0 =0
ad1=0
ad2 =0
ad3=0

lis0=[]
lis1=[]
lis2=[]
lis3=[]

for x in number:
	if x%a==0 and x%b != 0:
		lis0.append(x)
		ad0 +=x
	if x%b==0 and x%a !=0:
		lis0.append(x)
		ad1 +=x
	if x%b==0 and x%a ==0:
		lis2.append(x)
		ad2 +=x
	if x%b!=0 and x%a!=0:
		lis3.append(x)
		ad3 +=x

#Multiple of a not b
b = ''
for x in lis0:
	b += str(x)+' '

c = ''
for x in lis1:
	c += str(x)+' '

d = ''
for x in lis2:
	d += str(x)+ ' '

e = ''
for x in lis3:
	e += str(x)+' '

print(f'Numbers multiple of a not b are: {b} ==>', len(lis0))
print(f'Numbers multiple of b not a are: {c} ==>', len(lis1))
print(f'Numbers multiple of a and b are: {d} ==>', len(lis2))
print(f'Numbers that are neither multiple of a nor b are: {e} ==>', len(lis3))
