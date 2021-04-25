import sys
true=True
print ('game started')
print ('note press 0 to end press 2 to move farward press 3 to move left press 4 to move wright press 5 to move backwards press 6 to jump press 7 to save the game press 12 to open the calculator it can add and subtract to subtract type a negitive number the posititive number has to be largeer if you dont your rasult will be a negitive number')
while true:

#if i get stuck in a loop hit ctrl c
#how to open file. cd Documents, ls   

    n = int(input().strip())



    if (n > 1 and n<=2):
        print ('forward')

    elif (n > 2 and n<=3):
        print ('left')

    elif (n > 3 and n<=4):
        print('wright')

    elif (n > 4 and n<=5):
        print('backwards')

    elif (n > 5 and n<=6):
        print('jump')

    elif (n > 6 and n<=7):
        print('game saved')

    elif (n==0):
        print('game ended')
        sys.exit()

    elif (n==12):
    
        '''

        '''


        def add(a, b):
            c = a + b
            return c

        do_math = True
        while do_math:
            # take input from the user
            print('Enter an number:')
            a = int(input().strip())
            print('Enter another number:')
            b = int(input().strip())

            print('a: {} b: {}'.format(a, b))
            print('answer')
            print('tell me if the is wrong')
            # call the add function and print the results
            print(add(a,b))
            print()

            print('hope i was wright')
            print('Type "y" to play again and "n" to quit')
            print('made by travis and britney')
            response = input().strip()
            if response == 'y':
                print("Let's play again!")
            elif response == 'n':
                print('cammand stoped')
                # setting play to false will exit the while loop
                do_math = False
            else:
                print("Unrecognized response, guess you're playing again")
                print('note you cannot use letters')
                print('error')
            
    elif(n==1):
        print('this is not yet a command')
    

    else:
        print('blank')


