sis = [1,4,5,6]
#adding numbers to the list
sis.append(3)
sis.append(2)
sis.append(4)
sis.append(7)

#creating another list
sis2 = [3, 5, 3, 6, 8, 0]
#adding numbers to the second list
sis2.append(7)
sis2.append(2)

#print both lists 
print(sis)
print(sis2)
#multiply both lists 
products = [num1 * num2 for num1, num2 in zip(sis, sis2)]

#print out th product 
print(products)
#allocate memory from list
sis[2] = 3
sis2[2] = 0 
print(sis[2] * sis2[2])
