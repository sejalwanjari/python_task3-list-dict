print()

studentdata = [
    {
        'name' : 'Aaksh Sahare',
        'mob_no' : 347849,
        'address' : 'kalamna',
        'course' : 'data  analyst',
        'fees' : 45000,
        'batch' : 'da9'
    },
    {
        'name' : 'Vijay Verma',
        'mob_no' : 857294,
        'address' : 'itwari',
        'course' : 'Full stack development',
        'fees' : 55000,
        'batch' : 'da8'
    }
]


print('Student Information = ',studentdata)

print()


#copy() method

studentInformation = studentdata.copy()

print(f'ARC student data = ',studentInformation)

print()
print()

# get() method

studentmarks = {
        'name' : 'anjali',
        'maths' : 67,
        'science' : 58,
        'history' : 49,
        'hindi' : 76,
    }


print(f'marks of student = ', studentmarks)

history = studentmarks.get('history')
print()

print('history marks = ', history)
print()
print()

# clear() method

print(f'student marks before clear = ', studentmarks)

studentmarks.clear()
print()

print(f'student marks after clear = ',studentmarks)

print()
print()


# keys() method

Employeedata = {
    'emp_name' : 'Vijay Chavhan',
    'age' : 45,
    'designation' : 'data analyst',
    'mob_no' : 564598,
    'salary' : 150000,
    'address' : 'kalamna'
}

print(f'Employee Data = ',Employeedata)

Employee_info = Employeedata.keys()
print()

print(f'Employee data = ', Employee_info)

print()
print()


#pop() method

print(f'Employee data = ', Employeedata)

Employeedata.pop('address')
print()

print(f'Employee data = ', Employeedata)

print()
print()


# popitem() method

fruitsrate = {
    'mango' : 45,
    'banana' : 37,
    'apple' : 56,
    'pineapple' : 45,
    'cherry' : 55,
    'kiwi' : 56 
}

print(f'fruits rate before popitems = ', fruitsrate)

fruitsrate.popitem()
print()

print(f'fruits rate after popitems = ', fruitsrate)

print()
print()


# setdefault() method

print(f'fruits rate = ', fruitsrate)

cherry_rate = fruitsrate.setdefault('cherry', 55)

kiwi_rate = fruitsrate.setdefault('kiwi', 60)
print()

print(f'cherry rate = ', cherry_rate)
print(f'kiwi rate = ', kiwi_rate)

print()
print()


#update() method

print(f'employee data = ' , Employeedata)

Employeedata.update({'age' : 55})
print()

print(f'employee data = ', Employeedata)

print()
print()


# values() method

print(f'fruits rate = ' ,fruitsrate)

values = fruitsrate.values()
print()

print(f'fruits values = ', values)

print()
print()


# fromkeys() method

a = ('key1','key2','key3','key4')
b = None

dictionary = dict.fromkeys(a,b)

print(f'new dictionary = ',dictionary)

print()
print()


# items() method

top5students = {
    'sejal' : 'A+',
    'jagruti' : 'A+',
    'bhavik': 'A',
    'tamanna' : 'A',
    'prajakta' : 'B+'
}

print(f'top 5 students before = ', top5students)

top5 = top5students.items()
print()

top5students['prajakta'] = 'A'

print(f'top 5 students after = ', top5)
