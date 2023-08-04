# https://judge.softuni.org/Contests/Practice/Index/3592#0
def resolver(idx, expression):
    if expression[idx].isnumeric():
        return expression[idx]
    if expression[idx] == "t":
        return resolver(idx + 2, expression)
    elif expression[idx] == "f":
        counter = 0
        current_idx = idx + 1
        while True:
            if expression[current_idx] == "?":
                counter += 1
            elif expression[current_idx] == ":":
                counter -= 1
                if counter == 0:
                    return resolver(current_idx + 1, expression)
            current_idx += 1


expression = input().split()
print(resolver(0, expression))
