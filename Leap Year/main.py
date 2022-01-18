# 🚨 Check if its a leap year :) 
year = int(input("Which year do you want to check? "))
#Leap year if its even divided by 4 except if its even divided by 100 but if its also divided by 400 :) so %4= true %100 false %400 true :)

if (year % 4) == 0:

    if (year % 100 ) == 0: 
        if (year % 400) == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



