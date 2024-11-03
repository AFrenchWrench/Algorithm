def parse_system_equation(equation):
    """
    Parse a system of linear equation string into its coefficients.

    Args:
        equation (str): The system of linear equation to parse.

    Returns:
        tuple[int, int, int]: The coefficients a, b and c of the equation respectively.
    """
    
    # Extract the coefficient of x
    try:
        a = int(equation[: equation.index("x")])
    except ValueError:
        # If the coefficient of x is not specified, assume it is 1 or -1
        if equation[0] == "-":
            a = -1
        else:
            a = 1

    # Extract the coefficient of y
    try:
        b = int(equation[equation.index("x") + 1 : equation.index("y")])
    except ValueError:
        # If the coefficient of y is not specified, assume it is 1 or -1
        if equation[equation.index("x") + 1] == "-":
            b = -1
        else:
            b = 1
            
    # Extract the constant term
    c = int(equation[equation.index("=") + 1 :])

    return a, b, c


# Read two system of linear equations from the user
eq1 = input().lower()
eq2 = input().lower()

# Remove any whitespace from the equations
eq1 = eq1.replace(" ", "")
eq2 = eq2.replace(" ", "")

# Parse the coefficients of each equation
a1, b1, c1 = parse_system_equation(eq1)
a2, b2, c2 = parse_system_equation(eq2)


# Calculate the determinant of the system of equations
# ![](Q5nVN7zyZ4vfYQiD37ctU6i7fPe7etnR.svg)
det = a1 * b2 - a2 * b1

# Calculate the determinant of the system of equations in terms of x
det_x = (c1 * b2 - c2 * b1)

# Calculate the determinant of the system of equations in terms of y
det_y = (a1 * c2 - a2 * c1)

# Check if the system of equations has a solution
if det == 0:
    # If the determinant is 0, there is either no solution or an infinite number of solutions
    if det_x == 0 and det_y == 0:
        print("Infinite solution")
    else:
        print("No solution")
else:
    # Otherwise, solve for x and y
    x = det_x / det
    y = det_y / det
    
    # Print the solution
    print(f"x = {x:.2f}, y = {y:.2f}")
