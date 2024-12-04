#list, tupple, dictionary
#Dictionary collection of key value pairs
#Ordered collection of constants.

number = [1, 2, 4, 5, 6, 23]


okpa_list = ['Bambara nut', 'maggie', 'Palm oil', 'Vegetable']
print(okpa_list)

ingredient = input('Enter an Ingredient ')
okpa_list.append(ingredient)
print(okpa_list)

for item in okpa_list:
    if item == ingredient:
        print(f'{item} is in the list')