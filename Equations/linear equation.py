def parse_expression(expression, is_right_side=False):
    bs = []
    xs = []
    inc = 0
    start = 0

    for i in range(1, len(expression)):
        if expression[i] == "-" or expression[i] == "+":
            if "x" in expression[:i]:
                if expression[:i] == "-x":
                    xs.append(-1 if not is_right_side else 1)
                elif expression[:i] == "+x" or expression[:i] == "x":
                    xs.append(1 if not is_right_side else -1)
                else:
                    xs.append(int(expression[: i - 1]) * (-1 if is_right_side else 1))
            else:
                bs.append(int(expression[:i]) * (-1 if is_right_side else 1))
            start += i
            break

    for i in range(start, len(expression)):
        i += inc
        try:
            if expression[i] == "-" or expression[i] == "+":
                for j in range(i + 1, len(expression)):
                    if expression[j] == "-" or expression[j] == "+":
                        if "x" in expression[i:j]:
                            if expression[i:j] == "-x":
                                xs.append(-1 if not is_right_side else 1)
                            elif expression[i:j] == "+x":
                                xs.append(1 if not is_right_side else -1)
                            else:
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
                            if expression[i:] == "-x":
                                xs.append(-1 if not is_right_side else 1)
                            elif expression[i:] == "+x":
                                xs.append(1 if not is_right_side else -1)
                            else:
                                xs.append(
                                    int(expression[i:j]) * (-1 if is_right_side else 1)
                                )
                        else:
                            bs.append(
                                int(expression[i:]) * (-1 if is_right_side else 1)
                            )
                        inc += (j - i) - 1
        except IndexError:
            break

    return xs, bs


equation = input("Enter the equation: ")
equation = equation.replace(" ", "")

left_part, right_part = equation.split("=")

left_xs, left_bs = parse_expression(left_part)
right_xs, right_cs = parse_expression(right_part, is_right_side=True)

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
