grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
numbers =[5, 3, 3, 5, 4]
average = sum(numbers)/ len(numbers)
numbers_1=[2, 2, 2, 3]
average_1 = sum(numbers_1)/ len(numbers_1)
numbers_2 =[4, 5, 5, 2]
average_2 = sum(numbers_2) /len(numbers_2)
numbers_3 =[4, 4, 3]
average_3 = sum(numbers_3)/ len(numbers_3)
numbers_4 =[5, 5, 5, 4, 5]
average_4 = sum(numbers_4)/ len(numbers_4)
print(average)
print(average_1)
print(average_2)
print(average_3)
print(average_4)
middle_beam ={'Aaron': average, 'Bilbo': average_1, 'Johnny': average_2, 'Khendrik': average_3,'Steve': average_4}
print(middle_beam.get('Aaron'))
print(middle_beam.get('Bilbo'))
print(middle_beam.get('Johnny'))
print(middle_beam.get('Khendrik'))
print(middle_beam.get('Steve'))
print(middle_beam.items())


