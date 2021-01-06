import pyinputplus as pyip 

def addFunc(add,totalCost,addFunc):
        addingsChoice=pyip.inputMenu(list(addings.keys()),numbered=True,prompt='Which one?\n')
        totalCost+=addings[addingsChoice]
        del addings[addingsChoice]
        if len(addings)>1:
            add=pyip.inputYesNo(prompt='Do you want to add another one too?\n')
            if add=='yes':
                addFunc(add,totalCost,addFunc)

totalCost=0
breadType={'Wheat': 50,'White':70,'Sourdough':70}
proteinType={'Chicken':50,'Turkey':70,'Ham':80,'tofu':60}
cheezType={'Cheddar':10,'Swiss':15,'Mozarella':20}
addings = {'Mayo': 10, 'Mustard': 10, 'Lettuce': 5, 'Tomatoes': 5}

breadChoice=pyip.inputMenu(list(breadType.keys()),numbered=True, prompt='What type of bread do you prefer?\n')
totalCost+=breadType[breadChoice]

print()
proteinChoice=pyip.inputMenu(list(proteinType.keys()),numbered=True,prompt='What type of protein you want?\n')
totalCost+=proteinType[proteinChoice]

print()
cheese=pyip.inputYesNo(prompt='Want some cheese on top?\n')
if cheese=='yes':
    cheeseChoice=pyip.inputMenu(list(cheezType.keys()),numbered=True,prompt='What kind?\n')
    totalCost+=cheezType[cheeseChoice]

print()
add=pyip.inputYesNo(prompt='Do you want to add mayo, lettuce, mustard or tomatoes?\n')
if add=='yes':
    addFunc(add,totalCost,addFunc)

print()
numOfSandwich=pyip.inputNum(prompt="How many of these sandwiches would you like to order?\n",min=1)
totalCost*=numOfSandwich

print('--->Your total cost is Rs.'+str(totalCost)+'. Have a good day!')