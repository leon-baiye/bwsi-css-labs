"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """
    rlist = [0, "success"]
    if type(num1)== str or type(num2) == str:
        rlist[0] = "Invalid input. Please enter a number."
        rlist[1] = "error"
    else:
        if operation == "add":
            rlist[0] = str(num1 + num2)
        elif operation == "subtract":
            rlist[0] = str(num2 - num1)
        elif operation == "multiply":
            rlist[0] = str(num1 *num2)
        elif operation == "divide":
            if num2 != 0:
                rlist[0] = str(num1 / num2)
            else:
                rlist[0] = "Cannot divide by zero."
                rlist[1] = "error"
        else:
            rlist[0] = "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
            rlist[1] = "error"
    return rlist


def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    if result[1] == "success":
        print(f"The result of {operation}ing {num1} and {num2} is: {result[0]}")
    else:
        print("Error occured during calculation: ", result[0])

if __name__ == "__main__":
    main()
