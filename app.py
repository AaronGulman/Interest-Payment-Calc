def main():
        print("Welcome to the Interest Payment Calculator")
        print("")
        
        principal = float(input("Enter the amount borrowed: "))
        apr = input("Enter the annual interest rate: ")
        years = int(input("Enter teh duration of the loan(in years): "))
        
        
        monthly_interest_rate = apr / 1200
        number_of_months = years * 12 
        monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))
        
        