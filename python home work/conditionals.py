#Home work
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