



"""
We are trying to figure out which of these two salary options 
will make you more money.
Option one will make you 100 hundred dollars per day.
Option 2 will start of with one dollar and double every day.
Determine which option will pay you more. 
Use functions named option 1 and 2 to 
calculate the money earned.

"""

"""
if "option1" > "option2"
    print response
        "Option 1 is better"

if "option2" > "option1"
    print response 
        "option 2 is better"

if "option1" = "option2"
    print response 
        "option1" and "option2" pays the same

"""

def main():
 ## Compare salary options
 opt1 = option1()
 opt2 = option2()
 print("Option 1 = ${0:,.2f}.".format(opt1))
 print("Option 2 = ${0:,.2f}.".format(opt2))
 if opt1 > opt2:
    print("Option 1 pays better.")
 elif opt1 == opt2:
     print("Options pay the same.")
 else:
    print("Option 2 is better.")

 def option1():
     ## Compute the total salary for 10 days,
     ## with a flat salary of $100/day.
     sum = 0
     for i in range(10):
        sum += 100
     return sum

 def option2():
     ## Compute the total salary for 10 days,
     ## starting at $1 and doubling each day.
    sum = 0
    daySalary = 1
    for i in range(10):
    sum += daySalary
    daySalary *= 2
 return sum 