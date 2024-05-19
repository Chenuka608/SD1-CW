def range_checking(score, credit_type):
    while score not in credit_range:
        print("Out of range.")
        score = int(input(f"\nEnter your total {credit_type} credits:"))
    return score

def display_histogram(progress,trailer,retriever,exclude):
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
progress_list=[]
moduleT=[]
moduleR=[]
excludeL=[]
#getting the credit input from user

while valid:
    try:
        while valid:   #([valid = True ] this is an infinity loop which can be altered to stop)
        #validating whether user entered credits within the correct range
            credit_pass=0
            credit_defer=0
            credit_fail=0
            credit_tot=0
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
                progress_list.append(credit_pass)
                progress_list.append(credit_defer)
                progress_list.append(credit_fail)           

            elif(credit_pass==100):
                print("Progress (module trailer)")
                trailer+=1 
                moduleT.append(credit_pass)
                moduleT.append(credit_defer)
                moduleT.append(credit_fail)

            elif(credit_fail>=80 and credit_fail<=120):
                print("Exclude")
                exclude+=1 
                excludeL.append(credit_pass)
                excludeL.append(credit_defer)
                excludeL.append(credit_fail)
                
            else:
                print("module retriever")
                retriever+=1
                moduleR.append(credit_pass)
                moduleR.append(credit_defer)
                moduleR.append(credit_fail)
                
            #creating the menu option to user to choose whether to stop the program or continue with a new set of data
            
            option=str(input("\nWould you like to enter another set of data? \n Enter 'y ' for yes or 'q' to quit and view results :")).lower()
            if(option=='y'):
                continue

            elif(option=='q'):                              #creating the histogram by multiplying "*" with the incremented progression outcome counter
                display_histogram(progress,trailer,retriever,exclude)
                break

            else:
                while option not in ('q','y'):
                    print("invalid input pls enter again - ")
                    option = str(input("\nWould you like to enter another set of data? \n Enter 'y ' for yes or 'q' to quit and view results :")).lower()
                    if (option == "q"):
                        display_histogram(progress,trailer,retriever,exclude)
                        break
        print("Part 2\n")
        for i in range (0,len(progress_list),3):
            progress_slice=progress_list[i:i+3]
            progress_str=str(progress_slice).replace("[","").replace("]","")
            print("Progress -",progress_str)
            
        for i in range (0,len(moduleT),3):
            moduleT_slice=moduleT[i:i+3]
            moduleT_str=str(moduleT_slice).replace("[","").replace("]","")
            print("Progress (module trailer) - ",moduleT_str)
            
        for i in range (0,len(moduleR),3):
            moduleR_slice=moduleR[i:i+3]
            moduleR_str=str(moduleR_slice).replace("[","").replace("]","")
            print("module retriever - ",moduleR_str)
            
        for i in range (0,len(excludeL),3):
            excludeL_slice=excludeL[i:i+3]
            excludeL_str=str(excludeL_slice).replace("[","").replace("]","")
            print("Exclude - ",excludeL_str)

        break
                
    except ValueError:                  #Error handling in case entered values are not integer
        print("Integer Required")
    

