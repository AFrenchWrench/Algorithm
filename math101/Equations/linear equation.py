def parse_expression(expression, is_right_side=False):
    """
    Parses a linear equation expression into lists of coefficients for x and constant terms.

    Args:
        expression (str): The linear equation expression to parse.
        is_right_side (bool, optional): Whether the expression is on the right side of the equation. Defaults to False.

    Returns:
        tuple[list[int], list[int]]: The coefficients for x and constant terms respectively.
    """

    bs = []
    xs = []
    inc = 0
    start = 0

    # Parse the left side of the equation for x and constant terms
    for i in range(1, len(expression)):
        if expression[i] == "-" or expression[i] == "+":
            if "x" in expression[:i]:
                # If the expression starts with -x or +x, set the coefficient to -1 or 1 respectively
                if expression[:i] == "-x":
                    xs.append(-1 if not is_right_side else 1)
                elif expression[:i] == "+x" or expression[:i] == "x":
                    xs.append(1 if not is_right_side else -1)
                else:
                    # Otherwise, extract the coefficient from the expression
                    xs.append(int(expression[: i - 1]) * (-1 if is_right_side else 1))
            else:
                bs.append(int(expression[:i]) * (-1 if is_right_side else 1))
            start += i
            break

    # Parse the right side of the equation for x and constant terms
    for i in range(start, len(expression)):
        i += inc
        try:
            if expression[i] == "-" or expression[i] == "+":
                for j in range(i + 1, len(expression)):
                    if expression[j] == "-" or expression[j] == "+":
                        if "x" in expression[i:j]:
                            # If the expression contains -x or +x, set the coefficient to -1 or 1 respectively
                            if expression[i:j] == "-x":
                                xs.append(-1 if not is_right_side else 1)
                            elif expression[i:j] == "+x":
                                xs.append(1 if not is_right_side else -1)
                            else:
                                # Otherwise, extract the coefficient from the expression
                                xs.append(
                                    int(expression[i : j - 1])
                                    * (-1 if is_right_side else 1)
                                )
                        else:
                            bs.append(
                                int(expression[i:j]) * (-1 if is_right_side else 1)
                            )
                        inc += (j - i) - 1
                        break
                    elif (j + 1) == len(expression):
                        if "x" in expression[i:]:
                            # If the expression contains -x or +x, set the coefficient to -1 or 1 respectively
                            if expression[i:] == "-x":
                                xs.append(-1 if not is_right_side else 1)
                            elif expression[i:] == "+x":
                                xs.append(1 if not is_right_side else -1)
                            else:
                                # Otherwise, extract the coefficient from the expression
                                xs.append(
                                    int(expression[i:]) * (-1 if is_right_side else 1)
                                )
                        else:
                            bs.append(
                                int(expression[i:]) * (-1 if is_right_side else 1)
                            )
                        inc += (j - i) - 1
        except IndexError:
            break

    return xs, bs


equation = input("Enter the equation: ").lower()
equation = equation.replace(" ", "")

# Split the equation into left and right sides
left_part, right_part = equation.split("=")

# Parse the left side of the equation
left_xs, left_bs = parse_expression(left_part)
# Parse the right side of the equation
right_xs, right_cs = parse_expression(right_part, is_right_side=True)

# Calculate the coefficients for the equation
a = sum(left_xs + right_xs)
b = sum(left_bs)
c = -sum(right_cs)

if a == 0:
    if b != c:
        print("No solution")
    else:
        print("Infinite solution")
else:
    x = (c - b) / a
    print(f"{a}x + {b} = {c}")
    print(f"x={x:.2f}")
