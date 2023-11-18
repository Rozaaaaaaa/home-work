#task 1.

dog={ }


#task 2.
dog={'name:Karma','color:brown','breed:Beagle','legs:average','age:young'}

print(dog)


#task 3.


student_dictionary={
'first_name:Karl',
'last_name:Dixson',
'gender:boy',
'age:22',
'marital_status:single',
'skills:taekwando',
'country:Canada',
'city:Ottawo',
'address:Nasa street'
}

print(student_dictionary)

#task 4.

print(len(student_dictionary)) 




#task5 . 
student_dictionary={
    'skills:taekwando'
}
print(student_dictionary)
print(student_dictionary['skills']) 



#task 6.
student_dictionary['skills'].extend(['React', 'SQL'])

#task 7. 
keys_list = list(student_dictionary.keys())
print(f"Keys as a list: {keys_list}")

#task 8.
values_list = list(student_dictionary.values())
print(f"Values as a list: {values_list}")

#task 9.
items_list = list(student_dictionary.items())
print(f"Items as a list of tuples: {items_list}")

#task 10.
del student_dictionary['marital_status']

#task 11.
del dog