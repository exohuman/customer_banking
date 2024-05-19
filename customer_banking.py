# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

def get_numeric_input_with_validation(message):
    """Gets input and checks to see if it is a number, if it is then it returns
    the input string. If not, it shows a message indicating that the input is
    invalid.
    
    Args:
        message: The message displayed to the user when requesting their input.
    
    Returns:
        The string of what was requested from the user.
    """
    isValid = False
    while not isValid:
        input_str = input(message)
        # replace decimal since isdigit expects integer
        if input_str.replace('.', '').isdigit():
            isValid = True
        else:
            print("Please enter a decimal number with no special characters or letters.")
    return input_str


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(get_numeric_input_with_validation("Please enter your savings account balance: "))
    savings_interest = float(get_numeric_input_with_validation("Please enter the interest rate as a percentage: "))
    savings_maturity = int(get_numeric_input_with_validation("How many months: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"For {savings_maturity} months  |  Savings Interest Earned: {'{:.2f}'.format(interest_earned)}  |  Balance: {'{:.2f}'.format(updated_savings_balance)}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(get_numeric_input_with_validation("Please enter your CD account balance: "))
    cd_interest = float(get_numeric_input_with_validation("Please enter the CD interest rate as a percentage: "))
    cd_maturity = int(get_numeric_input_with_validation("How many months: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"For {cd_maturity} months  |  CD Interest Earned: {'{:.2f}'.format(interest_earned)}  |  Balance: {'{:.2f}'.format(updated_cd_balance)}")

if __name__ == "__main__":
    # Call the main function.
    main()