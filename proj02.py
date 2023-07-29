##############################################################################
# Computer Project 2
#
# start with a stock of coins (10 of each denomination)
# print a greeting
# prompt for price of an item or to quit
# if price input is negative, print an error and prompt again
# if valid price is input, prompt for dollars in payment
# if payment is less than price, print an error and prompt for another payment
# if payment equals price, print no change and halt program
# otherwise, use greedy algorithm to generate the change necessary
# while calculating change, keep track of the coins used and coin totals
# print change using minimum number of coins possible
# if change cannot be made using coins left, print error and halt program
# display number of each coin denomination remaining in the stock
# prompt for another price of an item or to quit
##############################################################################

# set initial stock to 10 per denomination
quarters = 10
dimes = 10
nickels = 10
pennies = 10

# set initial number of each denomination used to 0 
quarters_used = 0
dimes_used = 0
nickels_used = 0
pennies_used = 0

# print greeting and current stock of each coin denomination
print("Welcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

# prompt user to input a price
# quit the program if user enters 'q'
# break out of while loop if does not enter 'q'
# if user does not enter q, enter another while loop 
while True:
    price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
    if price_str == 'q':
        exit()
    else:
        break
        
price_int = int(float(price_str) * 100)

# determine if user entered payment price is negative
# if price entered is neg, print an error message
if price_int < 0: 
   print("\nError: purchase price must be non-negative.")
   print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
               quarters, dimes, nickels, pennies))
   # prompt user to enter another price and convert that to cents again
   price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
   price_int = int(float(price_str) * 100)
   
# determine if user entered string is 'q' 
# if so, halt the program
if price_str == 'q':
    exit()
    
payment_str = input("\nInput dollars paid (int): ") 
payment_int = int(float(payment_str) * 100) 

# determine if user entered payment is negative
# if payment entered is neg, print an error message
if payment_int < 0:
    print("\nError: purchase price must be non-negative.")
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
                quarters, dimes, nickels, pennies))
    payment_str = input("\nInput dollars paid (int): ") 
    payment_int = int(float(payment_str) * 100) 

# enter while loop when user enters a valid payment price that is not 'q'
# while loop tests code until it knows the price is valid to calculate change
while price_str != 'q':     
           
    price_int = int(float(price_str) * 100)
    # if the price entered is positive, prompt for a payment in dollars       
    if price_int > 0:
        payment_str = input("\nInput dollars paid (int): ") 
        payment_int = int(float(payment_str) * 100) 
        
        # if entered payment is less than price, print error and prompt again
        if payment_int < price_int:
            print("\nError: insufficient payment.")
            payment_str = input("\nInput dollars paid (int): ") 
            payment_int = int(float(payment_str) * 100)
            
        # if price and payment are the same, print no change and current stock
        # prompt the user for another purhcase price or to quit
        if price_int == payment_int:
            print("\nNo change.")
            print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
                        quarters, dimes, nickels, pennies))
            price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
            if price_str == 'q':
                exit()
            price_int = int(float(price_str) * 100)      

    # program has determined payment > price and change can be calculated
    # first, assign a variable to calculate change
    # subtract 25 until no longer possible, then 10, and so on
    # subtract coin from stock and add coin to amount used each time
    # this approach will calculate change using min. number of coins
    change = payment_int - price_int
    while change >= 25 and quarters >= 1:
        change -= 25
        quarters -= 1
        quarters_used += 1
    while change >= 10 and dimes >= 1:
        change -= 10
        dimes -= 1
        dimes_used += 1
    while change >= 5 and nickels >= 1:
        change -= 5
        nickels -= 1
        nickels_used += 1
        if nickels <= 0: # print error if not enough coins
            print("\nError: ran out of coins.")
            exit()
    while change >= 1 and pennies >= 1:
        change -= 1
        pennies -= 1
        pennies_used += 1
        if pennies <= 0: # print error if not enough coins
            print("\nError: ran out of coins.")
            exit()
  
    if change > 0:
        print("\nError: ran out of coins.")                
    
    # print change message
    # print number of coin used only if > 0
    print("\nCollect change below: ")
    if quarters_used > 0:
        print("Quarters:", quarters_used)
    if dimes_used > 0:
        print("Dimes:", dimes_used)
    if nickels_used > 0:
        print("Nickels:", nickels_used)
    if pennies_used > 0:
        print("Pennies:", pennies_used)
           
    # print the new stock and prompt for another purchase price
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
        quarters, dimes, nickels, pennies))
    price_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
            
    # reassign coins used for the next execution of loop
    # without doing this the program sums coins from previous loops
    quarters_used = 0
    dimes_used = 0
    nickels_used = 0
    pennies_used = 0


