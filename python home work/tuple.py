#Home work
#Level 1


#1
empty_tuple=()
print(empty_tuple)



#2
sisters=('Asel','Karlygash')
brothers=('Nursultan','Ersultan')



#3/4
siblings=sisters+brothers
print('Siblings:',  len(siblings))


#5
parents = ("Abdilhan", "Saule")
print(parents)

family_members = parents + siblings
print(family_members)



#Level 2
#1

family_members = parents + siblings
parents,siblings,*rest=family_members
print(parents)
print(siblings)
print(rest)




#2
fruits=('banana','apple','strawberry','peach','orange')
vegetables=('potato','carrot','tomato','cucumbers')
animal_products=('checken','beef','egg','milk')

food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)




#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)


#4?


#5
first_three_items = food_stuff_lt[:3]
print(first_three_items)



#6

food_stuff_tp = tuple(['banana', 'apple', 'strawberry', 'peach', 'orange', 'potato', 'carrot', 'tomato', 'cucumbers', 'checken', 'beef', 'egg', 'milk'])


del food_stuff_tp


#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print("true")
elif 'Iceland' in nordic_countries:
    print("False")


if 'Iceland' in nordic_countries:
    print("true")
else:
    print("false")
