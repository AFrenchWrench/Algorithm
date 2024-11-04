def pars_equation(equation):
    """
    Parses a quadratic equation string into its coefficients.

    Args:
        equation (str): The quadratic equation in the form "ax^2 + bx + c = 0".

    Returns:
        tuple[int, int, int]: The coefficients a, b, and c.
    """
    
    # Remove all whitespace from the equation
    equation = equation.replace(" ", "")
    # Convert the equation to lowercase
    equation = equation.lower()

    # Extract the coefficients a, b, and c from the equation
    a, b, c = (
        # Extract the coefficient of x^2
        (equation[: equation.index("x")]),
        # Extract the coefficient of x
        (equation[equation.index("x") + 3 : equation.rindex("x")]),
        # Extract the constant term
        int(equation[equation.rindex("x") + 1 : equation.index("=")])
    )

    # Handle the cases where the coefficients are not specified
    if a == "-":
        a = -1
    elif a == "":
        a = 1
    if b == "-":
        b = -1
    elif b == "+":
        b = 1

    # Return the coefficients as a tuple
    return int(a), int(b), c


# Read a quadratic equation from the user
equation = input()

# Parse the equation into its coefficients
a, b, c = pars_equation(equation)

# Calculate the discriminant
discriminant = (b * b) - (4 * a * c)

# Handle the different cases of the discriminant
if discriminant > 0:
    # If the discriminant is positive, the equation has two solutions
    print(f"x1={(-b + discriminant**0.5) / (2 * a)}")
    print(f"x2={(-b - discriminant**0.5) / (2 * a)}")
elif discriminant == 0:
    # If the discriminant is zero, the equation has one solution
    print(f"x={-b / (2 * a)}")
else:
    # If the discriminant is negative, the equation has no solutions
    print("No solution")

