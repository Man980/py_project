<<<<<<< HEAD
import os
name = 'Heloel'
length =int(len(name))-2
asterix = name[0]+'*'*length+name[-1]
while name != asterix:
	os.system('cls')
	print(asterix)
	a =input("antre let ki manke yo youn pa youn:\n>>> ")
	if a in name:
		index = name.find(a)
		asterix = asterix[:index] + a + asterix[index + 1:]
print(asterix)
	
=======
#this is a python project
>>>>>>> e85221269015fbfd6ec41c2d54463693098adc28
