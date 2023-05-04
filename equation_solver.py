import re  # Import the regular expression library to match patterns in strings

def parse_equation(equation):
    # Define a regular expression pattern that matches a linear equation in the form "ax + b = c"
    pattern = r'([-+]?\d*\.?\d*)([a-zA-Z])\s*([=])\s*([-+]?\d*\.?\d*)'
    
    # Match the pattern against the input equation
    match = re.match(pattern, equation)
    
    # If the pattern matches, extract the values of 'a' and 'b' from the matched groups and return them as floats
    if match:
        a = float(match.group(1)) if match.group(1) else 1.0  # If 'a' is not present in the input, assume it is 1.0
        b = float(match.group(4))
        return a, b
    else:  # If the pattern does not match, raise a ValueError with an error message
        raise ValueError('Invalid equation')

def solve_equation(equation):
    try:
        a, b = parse_equation(equation)  # Call the parse_equation function to extract 'a' and 'b' from the input
        
        # Check if the equation is linear (i.e., 'a' is not zero)
        if a == 0:
            if b == 0:  # If 'a' and 'b' are both zero, the equation has infinitely many solutions
                return 'The equation has infinitely many solutions'
            else:  # If 'a' is zero and 'b' is not zero, the equation has no solution
                return 'The equation has no solution'
        else:  # If 'a' is not zero, the equation has a unique solution
            x = (b - 0.0) / a  # Compute the value of 'x' by subtracting 'b' from both sides and dividing by 'a'
            steps = []  # Create an empty list to hold the steps of the solution
            steps.append(equation)  # Add the original equation to the list of steps
            steps.append(f'{a:.2f}x = {b-a:.2f}')  # Add the equation after subtracting 'b' from both sides
            steps.append(f'x = {x:.2f}')  # Add the equation after dividing by 'a'
            return '\n'.join(steps)  # Join the steps into a single string with newline characters between them
        
    except ValueError as e:  # If an error occurs during parsing, return the error message as a string
        return str(e)

def main():
    while True:
        equation = input('Enter an equation (or q to quit): ')  # Prompt the user to enter an equation
        if equation == 'q':  # If the user enters 'q', exit the loop
            break
        else:  # Otherwise, call the solve_equation function and print the result
            result = solve_equation(equation)
            print(result)

if __name__ == '__main__':
    main()