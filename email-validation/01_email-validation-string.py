email = input('Enter your Email: ')

k,j,d=0,0,0
if len(email)>6: #1
    if email[0].isalpha(): #2
        if ("@" in email) and (email.count("@")==1): #3 
            if (email[-3]==".") ^ (email[-4]=="."): #4
                for i in email:
                    if i.isspace(): #5
                        k=1
                    elif i.isalpha(): #5
                        if i ==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong Email: Contains space, uppercase letters, or invalid characters")
                else:
                    print("Email Accepted")
            else:
                print("Wrong Email: '.' should be at the 3rd or 4th position from the end")
        else:
            print("Wrong Email: '@' Should be used only once")
    else:
        print("Wrong Email: First letter should be an alphabet ")
else:
    print("Wrong Email: Length should be more than 6 characters")