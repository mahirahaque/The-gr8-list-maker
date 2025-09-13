import ast
print("❤️‍🔥WELCOME TO THIS PROGRAM WHERE LISTS WILL BE CREATED ACCORDING TO THE MENU OPTIONS BY THE USER INPUT❤️‍🔥")
print("MENU")
print("☛1. A list of the even integers in the entered list")
print("☛2. A list of the odd integers in the entered list.")
print("☛3. A list of the cubes of only the even integers appearing in the input list")
print("☛4. Quit")
while True:
    try:
            ch= ast.literal_eval(input("Enter a list: "))
    except:
        print("✖Please enter a list in form of [1,3,4,*,&,a,f,m] You can put anything in the list✖")
        continue

    
    choose=int(input("↘Enter a number from the menu↖: "))
    
    if choose==1:
        even=[n for n in ch if isinstance(n,int) and n%2 == 0 ]
        print(f"This is the obtained list {even} of even integers from the entered list✅")

    elif choose==2:
        odd=[n for n in ch if isinstance(n,int) and n%2 != 0 ]
        print(f"This is the obtained list {odd} of odd integers from the entered list✅")

    elif choose==3:
        cube=[n**3 for n in ch if isinstance(n,int) and n%2 == 0]
        print(f"This is the obtained list {cube} of cube of even integers from the entered list✅")

    elif choose==4:
        print("Thank you for using the program")
        break
    else:
        print("✖Please enter a number between 1-4✖")

        

        

        
        
    

        


    


