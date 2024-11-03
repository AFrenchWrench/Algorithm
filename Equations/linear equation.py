equation = input("Enter the equation: ")
equation = equation.replace(" ", "")

left_part, right_part = equation.split("=")

bs = []
xs = []
cs = []

inc = 0
start = 0

for i in range(1, len(left_part)):
    if left_part[i] == "-" or left_part[i] == "+":
        if "x" in left_part[:i]:
            if left_part[:i] == "-x":
                xs.append(-1)
            elif left_part[:i] == "+x" or left_part[:i] == "x":
                xs.append(1)
            else:
                xs.append(int(left_part[: i - 1]))
        else:
            bs.append(int(left_part[:i]))
        start += i
        break


for i in range(start, len(left_part)):
    i += inc

    try:
        if left_part[i] == "-" or left_part[i] == "+":
            for j in range(i + 1, len(left_part)):
                if left_part[j] == "-" or left_part[j] == "+":
                    if "x" in left_part[i:j]:
                        if left_part[i:j] == "-x":
                            xs.append(-1)
                        elif left_part[i:j] == "+x":
                            xs.append(1)
                        else:
                            xs.append(int(left_part[i : j - 1]))
                    else:
                        bs.append(int(left_part[i:j]))
                    inc += (j - i) - 1
                    break
                elif (j + 1) == len(left_part):
                    if "x" in left_part[i:]:
                        if left_part[i:] == "-x":
                            xs.append(-1)
                        elif left_part[i:] == "+x":
                            xs.append(1)
                        else:
                            xs.append(int(left_part[i:j]))
                    else:
                        bs.append(int(left_part[i:]))
                    inc += (j - i) - 1
    except IndexError:
        break

inc = 0
start = 0

for i in range(1, len(right_part)):
    if right_part[i] == "-" or right_part[i] == "+":
        if "x" in right_part[:i]:
            if right_part[:i] == "-x":
                xs.append(1)
            elif right_part[:i] == "+x" or right_part[:i] == "x":
                xs.append(-1)
            else:
                xs.append(-int(right_part[: i - 1]))
        else:
            cs.append(int(right_part[:i]))
        start += i
        break


for i in range(start, len(right_part)):
    i += inc

    try:
        if right_part[i] == "-" or right_part[i] == "+":
            for j in range(i + 1, len(right_part)):
                if right_part[j] == "-" or right_part[j] == "+":
                    if "x" in right_part[i:j]:
                        if right_part[i:j] == "-x":
                            xs.append(1)
                        elif right_part[i:j] == "+x":
                            xs.append(-1)
                        else:
                            xs.append(-int(right_part[i : j - 1]))
                    else:
                        cs.append(int(right_part[i:j]))
                    inc += (j - i) - 1
                    break
                elif (j + 1) == len(right_part):
                    if "x" in right_part[i:]:
                        if right_part[i:] == "-x":
                            xs.append(1)
                        elif right_part[i:] == "+x":
                            xs.append(-1)
                        else:
                            xs.append(-int(right_part[i:j]))
                    else:
                        cs.append(int(right_part[i:]))
                    inc += (j - i) - 1
    except IndexError:
        break


a = sum(xs)
b = sum(bs)
c = sum(cs)

if a == 0:
    if b != c:
        print("No solution")
    else:
        print("Infinite solution")
else:
    x = (c - b) / a

    print(f"{a}x + {b} = {c}")
    print(f"x={x:.2f}")
