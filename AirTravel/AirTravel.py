
def opening_statement():
    print("Aircraft Fuel Calculator\n\n")


def distance_calc():    #here we find the time the plane travels given the distance in nautical miles
    repeat = "y"
    while repeat == "y":
        userMiles=int(input("Distance in Nautical Miles: "))

        #formula to figure out the time when given the user input(nautical miles)
        timesDecimal=(userMiles / 120)      
        #print(timesDecimal)

        decimalTohours(timesDecimal)    #sends it to the definition that changes the times in decimal for into hours and minutes

        findFuel(timesDecimal)      #sends it the definition in order to find the fuel  consuption

        repeat=str(input("\n\nContinue? (y/n):"))
        print("")
    else:
        print("\nGoodbye!")


def decimalTohours(timesDecimal):
    TimesHours=int(timesDecimal)                                  #this takes the whole number digits to the left of the decimal point
    TimesMinutes=float((timesDecimal - int(timesDecimal))*60)     #this takes the decimal numbers and multiplies it with 60 in order to turn it from decimal into minutes
    print("Flight time: "+str(TimesHours)+" hour(s) and " +  str(round(TimesMinutes))+ " minute(s)")
     

def findFuel(timesDecimal):
    fuel_calc= (timesDecimal +0.5) *8.4    #the +0.5 is the extra 30 minutes, and is added before multiplying  so the extra 30 minutes is added to the times itself  
                                           #and not the number that comes out after the calculation
                                           #aka, after the multiplication we get the total gallomgs, so the 0.5 will add "0.5" gallongs, not "0.5" in time (0.5 = 30 minutes)


    fuel_wholeNumber=int(fuel_calc)                              #this takes the whole number digits to the left od the decimal point
    fuel_decimalNumber=float(fuel_calc - int(fuel_calc))         #this part takes the decimal numbers 
     
    wholePlusDecimal=fuel_wholeNumber + round(fuel_decimalNumber+0.05,1)           #this part add from the whole number and the decimals after "round(fuel_decimalNumber,1)"
                                                                                   #round the decimals up and to the 1 decimal place
                                                                                   #the 0.05 is so it can round up the decimal not downwards

    #print(fuel_decimalNumber)
    #print(round(fuel_decimalNumber+0.05,1))
    
    
    

    #print(round(fuel_decimalNumber+0.05,1))
    print("Required fuel: "+str(wholePlusDecimal)+" gallons")






def main():
    opening_statement()
    distance_calc()
    


if __name__ == "__main__":
    main()
