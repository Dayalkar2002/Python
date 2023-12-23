def add(x,y):
    add=x+y
    return (add)
print(add(5,5))
   

#Write a program using functions to Compute the monthly payment, given the loan amount, number of years and the annual interest rate.
loan_amount=int(input("enter the loan amount: "))
year=int(input("How many years:- "))*12

def emi(loan_amount,year):
     annual_interest=7

     total_interest=(loan_amount*annual_interest)/100
     print(f'The total interest on loan amount is {total_interest}')

     final_amount=loan_amount+total_interest
     print(f"The final_loan amount is {final_amount}")

     monthly_amount=final_amount//year
     print(f"The total monthly amount is {monthly_amount}")

emi(loan_amount,year)

    