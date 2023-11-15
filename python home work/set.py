#len-     барлық дубликатта жүреді      
#in-      тексереді   
#add-     жаңа элемент қосады , егер ол  SET ішінде болатын болса екінші рет қосылмайды ,себебі набордың ішінде екі элемент бірдей жүрмейді
#update-  набордың ішіне бірнеше элемент қосу,massive ,tuple,set
#pop-     рандомный элементті жояды набордан
#isdisjoin-    екеуінде ортақ элементтер бар 



# print(len(cities))

# cities.add('Seoul')
# print(len(cities))

# new_city= input("Enter a city:  ")
# cities.add(new_city)

# print( cities)


# new_city=input("Enter a  city: ")
# if  new_city in cities:
#     cities.remove(new_city)
#     print(f"{new_city} was removed  from the set")
# else:
#     print("No such city")



# cities={'Almaty','Rim','New-York','London','Aktobe'}

# new_cities=input("Enter a  city: ")
# print(new_cities)

# cities.update(new_cities.split())
# print(cities)





#level 1

#task 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))


#task 2    Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(len(it_companies))


#task 3   Insert multiple IT companies at once to the set it_companies

new_company={'Samsung','Huawei','Yandex'}
it_companies.update(new_company)
print(it_companies)



#task 4 Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)



#or
it_companies.remove('Huawei')
print(it_companies)



#task 5     What is the difference between remove and discard
#remove-элементтің тек біреуін өшіре аламыз
#discard- массивтің ішін немесе массивтың өзін өшіреді



#level 2

#task 1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
B.isdisjoint(A)
print(B)



#task 2   Find A intersection B

A.intersection(B)
print(A)


