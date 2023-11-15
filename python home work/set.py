
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
print(A.union(B))


#task 2   Find A intersection B
result = A.intersection(B)
print(result)


# #task 3
result= A.issubset(B)
print(result)


#task 4  Are A and B disjoint sets
print(A.isdisjoint(B))


#task 5 Join A with B and B with A
print(A.union(B))
print(B.union(A))



#task 6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#{28,27} -its symmetric difference between A and B




#task 7  Delete the sets completely
del A
del B



#Level 3
#task 1    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age=set(age)
print(age)
print(len(age))



#task 2    Explain the difference between the following data types: string, list, tuple and set

#string- өзгермейді,реттелген.
#list- өзгермелі, ретімен жүреді, қайталанатын дубликаттар тізіміне жатады
#tuple- элементтер өзгермейтін, қайталанатын дубликаттар тізіміне жатады
#set- ретсіз,индектелмеген жіне өзгертілмейтін жинақ,жаңа элементтер қоса аламыз,қайталанатын  дубликаттар тізіміне жатпайды.