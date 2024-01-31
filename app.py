def main():
        print("Welcome to the Interest Payment Calculator")
        print("")
        
        principal = float(input("Enter the amount borrowed: "))
        apr = float(input("Enter the annual interest rate: "))
        years = int(input("Enter the duration of the loan(in years): "))
        
        
        monthly_interest_rate = apr / 1200
        number_of_months = years * 12 
        monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))
        
        print("The monthly payment is: $" + str(round(monthly_payment, 2)))
        
main()