play = True

while play == True:
    name = input('What is your name?: ')
    print('hey', name)
    print('Welcome to the quest Game!')
    # Use \n to print the next statements on a new line
    print('1. wonderland \n2. Lala land')
    # wrap the input method with int() to convert to an integer
    choice = int(input('where would you like to go today?:'))
    if choice == 1:
        print('Welcome to wonderland!')
        print('there is lots to do here, but first you must say beetle juice 3 times')
        print('1. Say beetle juice to continue. \n2. quit game')
        first_choice = int(input('Would you like to continue?: '))
        if first_choice == 1:
            for i in range(3):
                print('Beetle juice')
                #input()
            print('great choice! Let us see how far you get.')
            colour = input('what is the colour of your fear (yellow or red): ')
            if colour == 'yellow'or 'blue':
                print("That's very mild you seem to fear nothing")   # you can't use single quote inside single quote, either double quote then single quote inside, or use \' will have the same effect
            elif colour == 'red':
                print('you have a lot of fears young one')
            else:
                print('Make the correct choice!')
        else:
            print('Thank you for playing!')
            play = False



    elif choice == 2:

        option2 = True

        while option2 == True:
            print('welcome to Lala land!')
            print('you look around you and you can see a dark forest on your left and the see ahead of you.')
            choice_1 = int(input('which way would you like to venture on? \ntype: 1. to go in the forest \n      2. to head to the see. \n      3. to return to the base.\n      type here : '))
            if choice_1 == 1:
                print('you decided to enter this dark and dense forest.' )
                print('you have walked for some time and you start to hear weird noises. \n ')
                print('What do you do? \nDo you go and inspect what those noises are (type 1) or you already are so scared and want return to lala land (type 2): \n')
                choice_1_1 = input('type inspect or return: ' )
                if choice_1_1 == 'inspect':
                    print('you are walking toward the noise, yet you hear some fast rustle in the bushes, you are pretty sure that you saw something moving in')

                else:
                    choice_1_1 = 'return'
                    print('So weak, you are returning to the base of the quest')
                    option2 = False

            elif choice_1 == 2:
                print('you are heading for the see')
            
            else:
                choice_1 != '1' or '2'
                print('You are returning to the base of the quest')
                option2 = False






    
