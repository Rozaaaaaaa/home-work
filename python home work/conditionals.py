#Home work
#LEVEL 1
#task 1
age=(int(input("Enter your age: ")))
if age <0:
    if age < -0:
        print("Its error")
elif age >=19:
    print("You're old enough to learn to drive")
else:
    print(f"You need {18-age} years to learn to drive")  




#task 2
age=(int(input("Enter your age: ")))
if age > 0 and age >=18:
    print("you're old enough to learn to drive  ")
elif age >0 and age <18:
    print(f"you need {18-age} years to leran to drive ")
else:
    print("Age should be greater than zero") 




#task 3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2: 
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is smaller than num2")
else:
    print("num1 is equal than to num2")



#LEVEL 2

#task 1 Write a code which gives grade to students according th their scores:

student=int(input("Enter your scores: "))
if 80 <= student <= 100:
    print("A")
elif 70 <= student <=89:
    print("B")
elif 60 <= student <=69:
    print("C") 
elif 50 <= student <=59:
    print("D")
elif 0 <= student <=49:
    print("F")
else:
    print("its error")   
   


#task 2
month=input("Enter a month: ")
if month =="june" or month=="july" or month=="august":
    print("The season is summer")
elif month=="march" or month=="april" or month=="may":
    print("The season is spring")
elif month=="september" or month=="octouber" or month=="november":
    print("The season is autumn")
else:
    print("The season is winter")


#task 3 ?
fruits = ['banana','orange','mango','lemon']
new_fruit = 'strawberry'
if new_fruit in fruits:
    print('That fruit already exist in the list')
else: 
    fruits.append(new_fruit)
    print(fruits)

#task 4
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['mother_name'] = 'Casy'
person['father_name'] = 'Lay'
person['skills'].append('Java')
person['age'] = 25
print(person)