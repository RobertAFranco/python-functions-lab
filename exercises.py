# Exercise 1

def calculate_area_triangle(base, height):
    return (base * height) / 2

print('Exercise 1:', calculate_area_triangle(10, 5))

# 2

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print('Exercise 2:', simple_interest(1000, 5, 2))

# 3

def apply_discount(price, discount_percentage):
    return price * (1 - discount_percentage / 100)

print('Exercise 3:', apply_discount(100, 25))

# 4

def convert_temperature(temp, unit):
    if unit == 'C':
        return (temp * 9 / 5) + 32
    elif unit == 'F':
        return (temp - 32) * 5 / 9
    else:
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit."

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# 5

def sum_to(n):
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6))

# 6

def largest(a, b, c):
    return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3))

# 7

def calculate_tip(bill_amount, tip_percentage):
    return (bill_amount * tip_percentage) / 100


print('Exercise 7:', calculate_tip(50, 20))

# 8

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print('Exercise 8:', product(2, 5, 5))

# 9

def basic_calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'."

print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))