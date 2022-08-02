#Exercice 1

#ip = input("Enter you IP address\n>>> ")
ip =input('Enter your IP address. egz: 192.168.192')
ip = ip.replace('.','')

first_letter = int(ip[0])
add =0
for x in ip:
	add +=int(x)
print(add*first_letter)

#Exercice 2
#As it is so simple, it is something made for beginners in a challenge

integer= int(input('Enter an enteger:\n>>> '))
if integer % 4 != 0:
	print('OK')
else:
	print('NOK')

