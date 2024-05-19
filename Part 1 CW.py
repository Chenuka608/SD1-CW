def range_checking(score, credit_type):      
    while score not in credit_range:
    ''' validates whether the credit_pass,credit_defer and credit_fail are in the correct range else it prints out of range
        and asks to re-enter until its within the range '''
        print("Out of range.")
        score = int(input(f"\nEnter your total {credit_type} credits:")) #f string format used in order to re enter the credit type if it was out of range
    return score

def display_histogram(progress,trailer,retriever,exclude):
     '''Displaying the histogram by multiplying '*' with the above counters'''
     print("\n","-"*60,"\nHistogram")
     print("Progress",progress," :",'*'*progress,"\nTrailer",trailer,"  :",'*'*trailer,"\nRetriever",retriever,":",'*'*retriever)
     print("Exclude",exclude,"  :",'*'*exclude,"\n")
     print(progress+retriever+trailer+exclude,"outcomes in total.\n","-"*60) 
    
    
#intializing the variables
credit_pass=0
credit_tot=0
credit_range=[0,20,40,60,80,100,120] #list of all the valid credit ranges to validate with user input
option=""
progress=0
trailer=0
retriever=0
exclude=0
valid=True

#getting the credit input from user

while valid:
    try:
        while valid:   #([valid = True ] this is an infinity loop which can be altered to stop)
        #validating whether user entered credits within the correct range
        
                                                #rangechecking(        score    , credit_type   )
            credit_pass=range_checking(int(input("\nEnter your total PASS credits:")),"PASS")       #prompting user to enter the credits at pass calling range_checking func
            credit_defer=range_checking(int(input("Enter your total DEFER credits:")),"DEFER")      #prompting user to enter the credits at defer calling range_checking func
            credit_fail=range_checking(int(input("Enter your total FAIL credits:")),"FAIL")         #prompting user to enter the credits at fail calling range_checking func
            
            credit_tot=credit_pass + credit_defer + credit_fail #calculating the credit total in order to check if its equal to 120
        
                #validating  whether the total is  120

            if(credit_tot!=120):
                print("Total incorrect.")
                continue

            #adding the progression outcome 
            if(credit_pass==120):
                print("Progress")
                progress+=1        

            elif(credit_pass==100):
                print("Progress (module trailer)")
                trailer+=1 
               
            elif(credit_fail>=80 and credit_fail<=120):
                print("Exclude")
                exclude+=1
                
            else:
                print("module retriever")
                retriever+=1
                
                
            #creating the menu option to user to choose whether to stop the program or continue with a new set of data
            
            option=str(input("\nWould you like to enter another set of data? \n Enter 'y ' for yes or 'q' to quit and view results :")).lower()
            if(option=='y'):
                continue

            elif(option=='q'):                              #creating the histogram by multiplying "*" with the incremented progression outcome counter
                display_histogram(progress,trailer,retriever,exclude)
                valid=False
                break

            else:
                while option not in ('q','y'):
                    print("invalid input pls enter again - ")
                    option = str(input("\nWould you like to enter another set of data? \n Enter 'y ' for yes or 'q' to quit and view results :")).lower()
                    if (option == "q"):
                        display_histogram(progress,trailer,retriever,exclude)
                        valid=False
                        break
                    
    except ValueError:
        print("Integer Required")
