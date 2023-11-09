#Home work

# Task 1
first= 'Thirty'
second = 'Days'
third = 'Of'
fourth = 'Python'
result = first + ' ' + second + ' ' + third + ' ' + fourth
print(result)


# Task 2 
white= 'Coding'
black='For'
yellow='All'
result=white+' '+black+' '+yellow
print(result)



# task 3/4/5
company = "Coding For All"
print(company)
print(len(company))




# task 6
company = "Coding For All"
company=company.upper()
print(company)


# task 7
company = "Coding For All"
company=company.lower()
print(company)


# task 8
# capitalize
company = 'Coding For All' 
print(company.capitalize())

# title
company = 'Coding For All' 
print(company.title())

# swapcase
company = 'Coding For All' 
print(company.swapcase())


# task 9
company = 'Coding For All' 
company=company.split(" ",1)[1]
print(company)



# task 10
company='Coding For All'
print(company.find('Coding'))


# task 11
company = 'Coding For All'
print(company.replace('Coding', 'Python'))


# task 12
company='Coding For All'
print(company.replace('Coding For All','Coding For Everyone'))


# task 13
company = 'Coding For All' 
print(company.split()) 


# task 14
company="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(company.split())



# task 15
company= "Coding For All"
result = company[0]
print(result)



# task 16
company = "Coding For All"
last_word = len(company) - 1
print(last_word)



# task 17
company = "Coding For All"
index = company[10]
print(index)



# task 18
company = "Python For Everyone"
words = company.split()
acronym = "".join(word[0] for word in words)
print(acronym)



# task 19
company = "Coding For All"
words = company.split()
acronym = "".join(word[0] for word in words)
print(acronym)


# task 20
company = 'Coding For All'
result = company.index('C')
print(f"The position of the first occurrence of 'C' in the string is: {result}")



# task 21
company = 'Coding For All'
result = company.index('F')
print(f"The position of the first occurrence of 'F' in the string is: {result}")



# task 22
company = 'Coding For All People'
result = company.rfind('l')
print(f"The position of the last occurrence of 'l' in the string is: {result}")




task 23
company = 'You cannot end a sentence with because because because is a conjunction'
result = company.index('because')  # we can use index or find
print(result)




# task 24
company = 'You cannot end a sentence with because because because is a conjunction'
last_position = company.rindex('because')

print(f"The position of the last occurrence of 'because' is: {last_position}")




# task 25/27
company='You cannot end a sentence with because because because is a conjunction'
last_slice=company[30:54]
print(last_slice)



# task 26
company = 'You cannot end a sentence with because because because is a conjunction'
position = company.find('because')
print(f"The position of the first occurrence of 'because' is: {position}")




# task  28
string = 'Coding For All'
company=string.startswith('Coding')
print(company)



# task 29
string = 'Coding For All'
company=string.endswith('Coding')
print(company)



# task 30
company = '   Coding For All      '
result = company.strip()
print(f"Original string: '{company}'")
print(f"Modified string: '{result}'")




# task 31
first= "30DaysOfPython"
second = "thirty_days_of_python"
print(first.isidentifier()) 
print(second.isidentifier())  



# task 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' # '.join(libraries)
print(result)



# task 33
sentence1 = "I am enjoying this challenge."
sentence2 = "I just wonder what is next."
combined_string = f"{sentence1}\n{sentence2}"
print(combined_string)



# task 34
print('Name\t\tAge\tCountry\t\tCity')
print('Asabeneh\t25\tFinland\t\tHelsinki')



# task 35
radius = 10
area = 3.14 * radius ** 2
output_string = f"The area of a circle with radius {radius} is {area} meters square."
print(output_string)



# task 36
a=8
b=6
print('{}+{}={}' .format(a,b, a+b))
print('{}-{}={}' .format(a,b, a-b))
print('{}*{}={}' .format(a,b, a*b))
print('{}/{}={}' .format(a,b, a/b))
print('{}%{}={}' .format(a,b, a%b))
print('{}//{}={}' .format(a,b, a//b))
print('{}*{}={}' .format(a,b, a*b))