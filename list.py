# 1.
list = []

# 2. 
my_list = [1, 2, 3, 4, 5, 6, 7]

# 3. 
list_len= len(my_list)

# 4.
first_item = my_list[0]
second_item = my_list[len(my_list)//2]
last_item = my_list[-1]

# 5. 
mixed_data_types = ['Roza Temirbai', 17, 165, 'single', 'Kazakhstan,Almaty,Ilysky']

# 6. 
it_companies = ['Google',  'Facebook',   'Apple','Microsoft' 'IBM', 'Oracle', 'Amazon']

# 7.
print("IT companies:", it_companies)

# 8.
print("Number of companies:", len(it_companies))

# 9.
print("First company:", it_companies[0])
print("second company:", it_companies[len(it_companies)//2])
print("Last company:", it_companies[-1])

# 10.
it_companies[1] = 'Twitter'
print("Updated list of IT companies:", it_companies)

# 11. 
it_companies.append('Intel')
print("List after adding a company:", it_companies)

# 12.
it_companies.insert(len(it_companies)//2, 'SAP')
print("List after inserting a company:", it_companies)

# 13. 
it_companies[3] = it_companies[3].upper()
print("List after changing a company name to uppercase:", it_companies)

# 14. 
joined_companies = '#; '.join(it_companies)
print("Joined companies:", joined_companies)

# 15. 
company_to_check = 'Microsoft'
if company_to_check in it_companies:
    print(f"{company_to_check} exists in the list.")

# 16.
it_companies.sort()
print("Sorted list of IT companies:", it_companies)

# 17.
it_companies.reverse()
print("Reversed list of IT companies:", it_companies)

# 18.
first_three_companies = it_companies[:3]
print("First three companies:", first_three_companies)

# 19. 
last_three_companies = it_companies[-3:]
print("Last three companies:", last_three_companies)

#task 20
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.remove('Apple')
print(it_companies)


#task 21
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.remove('Facebook')
print(it_companies)


#task 22
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.remove('Apple')
print(it_companies)


#task 23
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.remove('Amazon')
print(it_companies)


#task 24
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.clear('it_companies')
print(it_companies)



#task 26
front_end= ['HTML', 'CSS', 'JavaScript', 'React','Redux']
back_end=['Node','Express','Mongodb']
result = front_end+back_end
print(result) # 'HTML CSS JavaScript React'











#LEVEL 2
#task 1
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print("min=",min(ages))
print("max=",max(ages))



#2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("min=",min(ages))
print("max=",max(ages))

 
#3
countries = ['China','Russia','USA','Finland','Sweden','Norway','Denmark']
first_country, second_country, third_country, *rest = countries
print(first_country)
print(second_country)
print(third_country)
print(rest)






