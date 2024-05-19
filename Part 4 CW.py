# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20221022
 
# Date: 25/3/2023

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
progression_dict={}

#getting the credit input from user

while valid:
    try:
        while valid:   #([valid = True ] this is an infinity loop which can be altered to stop)
            #validating whether user entered credits within the correct range
        
            student_ID=str(input("\nEnter your student ID :"))
            if(student_ID[0]=='w') and len(student_ID)==8 :
                pass
            else:
                print("Invalid student ID ")
                continue                                      #rangechecking(        score    , credit_type   )
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
                
                progression_dict[student_ID]=("Progress -", credit_pass,credit_defer,credit_fail)   

            elif(credit_pass==100):
                print("Progress (module trailer)")
                
                progression_dict[student_ID]=("Progress (module trailer) -", credit_pass,credit_defer,credit_fail,)      

            elif(credit_fail>=80 and credit_fail<=120):
                print("Exclude")
                progression_dict[student_ID]=("Exclude -",credit_pass,credit_defer,credit_fail)            
                
            else:
                print("module retriever")
                progression_dict[student_ID]=("module retriever -", credit_pass,credit_defer,credit_fail)
    
                
            #creating the menu option to user to choose whether to stop the program or continue with a new set of data
            
            option=str(input("\nWould you like to enter another set of data? \nEnter 'y ' for yes or 'q' to quit and view results :")).lower()
            if(option=='y'):
                continue

            elif(option=='q'):                       
                 print("\nPart4 \n",progression_dict)
                 valid=False
                 break

            else:
                while option not in ('q','y'):
                    print("invalid input pls enter again - ")
                    option = str(input("\nWould you like to enter another set of data? \n Enter 'y ' for yes or 'q' to quit and view results :")).lower()
                    if (option == "q"):
                        print("\nPart4\n",progression_dict)
                        valid=False
                        break     
                        
    except ValueError:                  #Error handling in case entered values are not integer
        print("Integer Required")
    

