firstInput = float(input('First '));
secondInput = float(input('Second '));
sum =  str(firstInput + secondInput)
print('Sum is ' + sum);

sumArray = []
sumArray.insert(0, sum)
print(sumArray)


name = input('What is your name? ')
print('Hello ' + name)
item = input('What do you want? Rice, Beans ')


if item == "Beans" : 
    print('Thank you ' + name);
    print('You can pick your ' + item)
elif item == "Rice": 
    print("Nice!! You've picked rice. You can pick it at the delivery section.")
else : 
    print("Sorry We don't have " + item + ' in the cart feel free to check back later')

print('Thank you for using my python App. Feel free to comeback next time')