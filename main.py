import math
def format_answer(answer):
    if answer.is_integer():
        return int(answer)
    else:
        return answer
def scientific_calculator():
    print("\nScientific Calculator")
    print("1. Square")
    print("2. Cube")
    print("3. Power")
    print('4. Square Root')
    print('5. Factorial')
    print('6. Percentage')
    print('7. Sine')
    print('8. Cosine')
    print('9. Tangent')
    print('10. Logarithm')
    print('11. Remainder')
    scientific_choice = input("Enter your choice: ")
    try:
        num = float(input("Enter a number: "))
    except:
        print("Invalid input. Please enter a valid number.")
        return

    if scientific_choice == "1":
        answer = num * num
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = str(num) + " ^ 2 = " + str(answer)
        add_to_history(calculation)
    
    elif scientific_choice == "2":
        answer = num ** 3
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = str(num) + " ^ 3 = " + str(answer)
        add_to_history(calculation)
    elif scientific_choice == "3":
        try:
            power = float(input("Enter the power: "))
        except:
            print("Invalid input. Please enter a valid number.")
            return
        answer = num ** power
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = str(num) + " ^ " + str(power) + " = " + str(answer)
        add_to_history(calculation)
                
    elif scientific_choice == "4":
        if num <0:
            print('Cannot find square root of a negative number.')
        else:
            answer = num ** 0.5
            answer = format_answer(answer)
            print("Answer:", answer)
            calculation = str(num) + " ^ 0.5 = " + str(answer)
            add_to_history(calculation)
                    
    elif scientific_choice == "5":
        if num < 0:
            print('Factorial is only defined for positive integers.')
        elif not num.is_integer():
            print('Factorial is only defined for positive integers.')
        else:
            factorial = 1
    
            for i in range(1, int(num) + 1):
                factorial = factorial * i
    
                print("Answer:", factorial)
                calculation = str(num) + "! = " + str(factorial)
                add_to_history(calculation)
    
    elif scientific_choice == "6":
        try:
            percentage = float(input("Enter the percentage: "))
        except:
            print("Invalid input. Please enter a valid number.")
            return
        answer = (num * percentage) / 100
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = str(num) + " * " + str(percentage) + " / 100 = " + str(answer)
        add_to_history(calculation)

    elif scientific_choice == "7":
        answer = math.sin(math.radians(num))
        answer = round(answer, 4)
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = "sin(" + str(num) + ") = " + str(answer)
        add_to_history(calculation)
    
    elif scientific_choice == "8":
        answer = math.cos(math.radians(num))
        answer = round(answer, 4)
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = "cos(" + str(num) + ") = " + str(answer)
        add_to_history(calculation)

    elif scientific_choice == "9":
        answer = math.tan(math.radians(num))
        answer = round(answer, 4)
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = "tan(" + str(num) + ") = " + str(answer)
        add_to_history(calculation)
    
    elif scientific_choice == "10":
        print("1. Log base 10")
        print("2. Natural log")
        try:
            log_choice = input("Enter your choice: ")
        except:
            print("Invalid input. Please enter a valid number.")
            return

        if log_choice == "1":
            if num <= 0:
                print('Logarithm is only defined for positive numbers.')
            else:
                answer = math.log10(num)
                answer = format_answer(answer)
                print("Answer:", answer)
                calculation = "log10(" + str(num) + ") = " + str(answer)
                add_to_history(calculation)
        elif log_choice == "2":
            if num <= 0:
                print('Logarithm is only defined for positive numbers.')
            else:
                answer = math.log(num)
                answer = format_answer(answer)
                print("Answer:", answer)
                calculation = "ln(" + str(num) + ") = " + str(answer)
                add_to_history(calculation)
        else:
            print("Invalid operation")
                        
    elif scientific_choice == "11":
        try:
            num2 = float(input("Enter the second number: "))
        except:
            print("Invalid input. Please enter a valid number.")
            return

        if num2 == 0:
            print("Cannot find remainder with zero.")
        else:
            answer = num % num2
            answer = format_answer(answer)
            print("Answer:", answer)
            calculation = str(num) + " % " + str(num2) + " = " + str(answer)
            add_to_history(calculation)
def linear_equation():
    print("\nLinear Equation Solver")
    print('1. One Variable')
    print('2. Two Variables')
    print('3. Three Variables')
    print('4. Back')
    choice = input("Enter your choice: ")
    if choice == "1":
        linear_one_variable()
    elif choice == "2":
        linear_two_variables()
    elif choice == "3":
        linear_three_variables()
    elif choice == "4":
        return
    else:
        print("Invalid choice")
def linear_one_variable():
    print("\nEquation Solver")
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
    except:
        print("Invalid input. Please enter valid numbers.")
        return

    a_display = format_answer(a)
    b_display = format_answer(b)
    c_display = format_answer(c)
    if a == 0:
        print('a cannot be zero.')
        return
    else:
        x = (c - b) / a
    print('\nSteps:')
    print(str(a_display) + " * x + " + str(b_display) + " = " + str(c_display))
    print(str(a_display) + " * x = " + str(c_display) + " - " + str(b_display))
    print(str(a_display) + " * x = " + str(c_display - b_display))
    print('x =', format_answer(x))
    calculation = str(a_display) + " * x + " + str(b_display) + " = " + str(c_display) + " => x = " + str(format_answer(x))
    add_to_history(calculation)
def linear_two_variables():
    print("\nTwo Variable Linear Equation Solver")
    print("Equation 1: ax + by = c")
    print("Equation 2: dx + ey = f")
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = float(input("Enter d: "))
        e = float(input("Enter e: "))
        f = float(input("Enter f: "))
    except:
        print("Invalid input. Please enter valid numbers.")
        return

    if a == 0:
        print("Cannot eliminate x using this method.")
        return

    denominator = b * d - a * e
    if denominator == 0:
        print("The system has no unique solution.")
        return
    y = (c * d - a * f) / denominator
    x = (c - b * y) / a
    x = format_answer(x)
    y = format_answer(y)

    print('\nSteps:')
    print(str(a) + " * x + " + str(b) + " * y = " + str(c))
    print(str(d) + " * x + " + str(e) + " * y = " + str(f))
    print('\nAfter eliminating x:')
    print('y =', y)
    print('\nSubstitute y back:')
    print('x =', x)
    calculation = str(a) + "x + " + str(b) + "y = " + str(c) + "; " + str(d) + "x + " + str(e) + "y = " + str(f) + " => x = " + str(x) + ", y = " + str(y)
    add_to_history(calculation)
def linear_three_variables():
    print("\nThree Variable Linear Equation Solver")
    print("Equation 1: ax + by + cz = d")
    print("Equation 2: ex + fy + gz = h")
    print("Equation 3: ix + jy + kz = l")
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = float(input("Enter d: "))
        e = float(input("Enter e: "))
        f = float(input("Enter f: "))
        g = float(input("Enter g: "))
        h = float(input("Enter h: "))
        i = float(input("Enter i: "))
        j = float(input("Enter j: "))
        k = float(input("Enter k: "))
        l = float(input("Enter l: "))
    except:
        print("Please enter valid numbers.")
        return
    denominator = (a * (f * k - g * j)- b * (e * k - g * i)+ c * (e * j - f * i) )

    if denominator == 0:
        print("The system has no unique solution.")
        return
    x = ((d * (f * k - g * j) - b * (h * k - g * l) + c * (h * j - f * l)) / denominator)
    y = ((a * (h * k - g * l) - d * (e * k - g * i) + c * (e * l - h * i)) / denominator)
    z = ((a * (f * l - h * j) - b * (e * l - h * i) + d * (e * j - f * i)) / denominator)
    x = format_answer(x)
    y = format_answer(y)
    z = format_answer(z)
    print('x =', x)
    print('y =', y)
    print('z =', z)
    calculation = str(a) + "x + " + str(b) + "y + " + str(c) + "z = " + str(d) + "; " + str(e) + "x + " + str(f) + "y + " + str(g) + "z = " + str(h) + "; " + str(i) + "x + " + str(j) + "y + " + str(k) + "z = " + str(l) + " => x = " + str(x) + ", y = " + str(y) + ", z = " + str(z)
    add_to_history(calculation)
def quadratic_equation():
    print("\nQuadratic Equation Solver")
    print("Equation: ax^2 + bx + c = 0")
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
    except:
        print("Please enter valid numbers.")
        return
    if a == 0:
        print('This is not a quadratic equation.')
        return
    discriminant = b ** 2 - 4 * a * c
    print('Discriminant =', discriminant)
    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        root1 = format_answer(root1)
        root2 = format_answer(root2)
        print('Roots are real and different.')
        print('Root 1 =', root1)
        print('Root 2 =', root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        root = format_answer(root)
        print('Roots are real and same.')
        print('Root =', root)
    else:
        real_part = -b / (2 * a)
        imaginary_part = (abs(discriminant) ** 0.5) / (2 * abs(a))
        real_part = format_answer(real_part)
        imaginary_part = format_answer(imaginary_part)
        print('Roots are complex and different.')
        print('Root 1 =', str(real_part) + ' + ' + str(imaginary_part) + 'i')
        print('Root 2 =', str(real_part) + ' - ' + str(imaginary_part) + 'i')
    a_display = format_answer(a)
    b_display = format_answer(b)
    c_display = format_answer(c)
    if b<0:
        b_text = '-' + str(abs(b_display))
    else:
        b_text = '+' + str(b_display)
    if c<0:
        c_text = '-' + str(abs(c_display))
    else:
        c_text = '+' + str(c_display)

    calculation = str(a_display) + "x^2 + " + str(b_text) + "x + " + str(c_text) + " = 0 => Roots: "
    if discriminant > 0:
        calculation +=  str(root1) + ", " + str(root2)
    elif discriminant == 0:
        calculation += str(root)
    else:
        calculation += str(real_part) + " + " + str(imaginary_part) + "i, " + str(real_part) + " - " + str(imaginary_part) + "i"
    add_to_history(calculation)
def cubic_value(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d
def find_cubic_roots(a, b, c, d):
    roots = []
    discriminant = (2*b)**2 - 4*3*a*c
    points = [-100, 100]
    if discriminant >= 0:
        x1 = (-2*b + discriminant**0.5) / (2*3*a)
        x2 = (-2*b - discriminant**0.5) / (2*3*a)
        if -100 <= x1 <= 100:
            points.append(x1)
        if -100 <= x2 <= 100:
            points.append(x2)
    points.sort()
    for x in points[1:-1]:
        value = cubic_value(a,b,c,d,x)
        if abs(value) < 0.000001:
            roots.append(round(x,3))
    for i in range(len(points) - 1):
        left = points[i]
        right = points[i+1]
        left_value = cubic_value(a,b,c,d,left)
        right_value = cubic_value(a, b, c, d, right)

        if left_value * right_value < 0:
            while right - left > 0.000001:
                middle = (left + right) / 2
                middle_value = cubic_value(a, b, c, d, middle)

                if left_value * middle_value < 0:
                    right = middle
                    right_value = middle_value
                    
                else:
                    left = middle
                    left_value = middle_value
            root = round((left+right)/2, 3)
            if root not in roots:
                roots.append(root)
    roots.sort()
    return roots
def cubic_equation():
    print("\nCubic Equation Solver")
    print("Equation: ax^3 + bx^2 + cx + d = 0")
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        d = float(input("Enter d: "))
    except:
        print("Please enter valid numbers.")
        return
    if a == 0:
        print('This is not a cubic equation.')
        return
    roots = find_cubic_roots(a, b, c, d)
    if len(roots) == 0:
        print('No real roots found.')
    else:
        print('Real roots found:')
        for root in roots:
            root = round(root, 3)
            root = format_answer(float(root))
            print(root)
    a_display = format_answer(a)
    b_display = format_answer(b)
    c_display = format_answer(c)
    d_display = format_answer(d)

    calculation = str(a_display) + "x^3 + " + ( '-' + str(abs(b_display)) if b < 0 else '+' + str(b_display) ) + "x^2 + " + ( '-' + str(abs(c_display)) if c < 0 else '+' + str(c_display) ) + "x + " + ( '-' + str(abs(d_display)) if d < 0 else '+' + str(d_display) ) + " = 0 => Roots: "
    calculation += ',' .join([str(format_answer((round(root, 3)))) for root in roots])
    add_to_history(calculation)
def equation_solver():
    print("\nEquation Solver")
    print("1. Linear Equation")
    print("2. Quadratic Equation")
    print("3. Cubic Equation")
    print("4. Back")

    choice = input("Enter your choice: ")

    if choice == "1":
        linear_equation()

    elif choice == "2":
        quadratic_equation()

    elif choice == "3":
        cubic_equation()

    elif choice == "4":
        return

    else:
        print("Invalid choice")


def basic_calculator():
    print("\nBasic Calculator")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num1_display = format_answer(num1)
        num2_display = format_answer(num2)
    
    except:
        print("Please enter valid numbers.")
        return
    
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice: ")
    if choice == "1":
        answer = num1 + num2
        answer = format_answer(answer)
        print("Answer:",answer)
        calculation = str(num1_display) + " + " + str(num2_display) + " = " + str(answer)
        history.append(calculation)
        save_history(calculation)
    
    elif choice == "2":
        answer = num1 - num2
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = str(num1_display) + " - " + str(num2_display) + " = " + str(answer)
        history.append(calculation)
        save_history(calculation)
    
    elif choice == "3":
        answer = num1 * num2
        answer = format_answer(answer)
        print("Answer:", answer)
        calculation = str(num1_display) + " * " + str(num2_display) + " = " + str(answer)
        history.append(calculation)
        save_history(calculation)
    
    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            answer = num1 / num2
            answer = format_answer(answer)
            print("Answer:", answer)
            calculation = str(num1_display) + " / " + str(num2_display) + " = " + str(answer)
            history.append(calculation)
            save_history(calculation)
history = []
try:
    file = open("history.txt", "r")
    for line in file:
        history.append(line.strip())
    file.close()
except:
      pass
def view_history():
    print("\nCalculation History:")
    if len(history) == 0:
        print("No calculations yet.")
    else:
        for calculation in history:
            print(calculation)
def save_history(calculation):
    file = open("history.txt", "a")
    file.write(calculation + "\n")
    file.close()
def add_to_history(calculation):
    history.append(calculation)
    save_history(calculation)
def clear_history():
    confirmation = input("Are you sure you want to clear the history? (y/n): ").lower()
    if confirmation == "y" or confirmation == "yes":
        history.clear()
        file = open("history.txt", "w")
        file.close()
        print('History cleared successfully.')
    else:
        print('History was not cleared.')
def length_converter():
    print("\nLength Converter")
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            kilometers = float(input("Enter distance in kilometers: "))
            miles = kilometers * 0.621371
            miles = format_answer(miles)
            print('Answer:', miles, 'miles')
            calculation = str(kilometers) + " km = " + str(miles) + " miles"
            add_to_history(calculation)
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        try:
            miles = float(input("Enter distance in miles: "))
            kilometers = miles / 0.621371
            kilometers = format_answer(kilometers)
            print('Answer:', kilometers, 'kilometers')
            calculation = str(miles) + " miles = " + str(kilometers) + " km"
            add_to_history(calculation)
        except:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid operation")
def weight_converter():
    print("\nWeight Converter")
    print('1. Kilograms to Pounds')
    print('2. Pounds to Kilograms')
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            kilograms = float(input("Enter weight in kilograms: "))
            pounds = kilograms * 2.20462
            pounds = format_answer(pounds)
            print('Answer:', pounds, 'pounds')
            calculation = str(kilograms) + " kg = " + str(pounds) + " pounds"
            add_to_history(calculation)
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        try:
            pounds = float(input("Enter weight in pounds: "))
            kilograms = pounds / 2.20462
            kilograms = format_answer(kilograms)
            print('Answer:', kilograms, 'kilograms')
            calculation = str(pounds) + " pounds = " + str(kilograms) + " kg"
            add_to_history(calculation)
        except:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid operation")
def temperature_converter():
    print("\nTemperature Converter")
    print('1. Celsius to Fahrenheit')
    print('2. Fahrenheit to Celsius')
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            fahrenheit = format_answer(fahrenheit)
            calculation = str(celsius) + "°C = " + str(fahrenheit) + "°F"
            add_to_history(calculation)
            print('Answer:', fahrenheit, 'Fahrenheit')
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            celsius = format_answer(celsius)
            calculation = str(fahrenheit) + "°F = " + str(celsius) + "°C"
            add_to_history(calculation)
            print('Answer:', celsius, 'Celsius')
        except:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid operation")
def time_converter():
    print("\nTime Converter")
    print('1. Hours to Minutes')
    print('2. Minutes to Hours')
    print('3. Minutes to Seconds')
    print('4. Seconds to Minutes')
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            hours = float(input("Enter time in hours: "))
            minutes = hours * 60
            minutes = format_answer(minutes)
            calculation = str(hours) + " hours = " + str(minutes) + " minutes"
            add_to_history(calculation)
            print('Answer:', minutes, 'minutes')
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        try:
            minutes = float(input("Enter time in minutes: "))
            hours = minutes / 60
            hours = format_answer(hours)
            calculation = str(minutes) + " minutes = " + str(hours) + " hours"
            add_to_history(calculation)
            print('Answer:', hours, 'hours')
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == "3":
        try:
            minutes = float(input("Enter time in minutes: "))
            seconds = minutes * 60
            seconds = format_answer(seconds)
            calculation = str(minutes) + " minutes = " + str(seconds) + " seconds"
            add_to_history(calculation)
            print('Answer:', seconds, 'seconds')
        except:
            print("Invalid input. Please enter a valid number.")
    elif choice == "4":
        try:
            seconds = float(input("Enter time in seconds: "))
            minutes = seconds / 60
            minutes = format_answer(minutes)
            calculation = str(seconds) + " seconds = " + str(minutes) + " minutes"
            add_to_history(calculation)
            print('Answer:', minutes, 'minutes')
        except:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid operation")
def unit_converter():
    print("\nUnit Converter")
    print('1. Length')
    print('2. Weight')
    print('3. Temperature')
    print('4. Time')
    choice = input("Enter your choice: ")
    if choice == "1":
        length_converter()
    elif choice == "2":
        weight_converter()
    elif choice == "3":
        temperature_converter()
    elif choice == "4":
        time_converter()
    else:
        print("Invalid operation")
def expense_tracker():
    print('\nStudent Expense Tracker')
    
    try:
        file = open("pocket_money.txt", "r")
        pocket_money = float(file.read())
        file.close()

        print("Saved pocket money:", pocket_money)

        change = input("Do you want to update it? (yes/no): ")

        if change.lower() == "yes":
            try:
                new_pocket_money = float(input("Enter your new pocket money: "))

                if new_pocket_money < 0:
                    print("Pocket money cannot be negative.")
                    return
                pocket_money = new_pocket_money

                file = open("pocket_money.txt", "w")
                file.write(str(pocket_money))
                file.close()
            except ValueError:
                print('Invalid input: Please enter a number.')
                return 

    except FileNotFoundError:
        try:
            pocket_money = float(input("Enter your pocket money: "))

            if pocket_money < 0:
                print("Pocket money cannot be negative.")
                return

            file = open("pocket_money.txt", "w")
            file.write(str(pocket_money))
            file.close()

        except ValueError:
            print("Invalid input! Please enter a number.")
            return

    except ValueError:
        print("Invalid saved pocket money.")
        return

    expense_history = []
    try:
        file = open("expense_history.txt", "r")

        for line in file:
            expense_history.append(line.strip())

        file.close()

    except FileNotFoundError:
        pass

    total_expenses = 0
    food_expenses = 0
    travel_expenses = 0
    shopping_expenses = 0
    other_expenses = 0
    for item in expense_history:
        parts = item.split(" | Category: ")

        amount_text = parts[0].replace("Rs. ", "")
        amount = float(amount_text)
        category_name = parts[1]

        total_expenses += amount

        if category_name == "Food":
            food_expenses += amount
        elif category_name == "Travel":
            travel_expenses += amount
        elif category_name == "Shopping":
            shopping_expenses += amount
        elif category_name == "Others":
            other_expenses += amount

    while True:
        print('\n1. Add Expense')
        print('2. View Balance')
        print('3. View Expense History')
        print('4. Back')
        choice = input('Enter your choice:')
        if choice == '1':
            try:
                expense = float(input('Enter expense amount: '))
            except ValueError:
                print('Invalid input! Please enter a number.')
            if expense <= 0:
                print('Please enter a valid amount.')
                continue
            else:
                print('\nExpense Categories')
                print('1. Food')
                print("2. Travel")
                print('3. Shopping')
                print('4. Others')
                category = input('Choose category:')
                if category == '1':
                    food_expenses += expense
                    category_name = 'Food'
                elif category == '2':
                    travel_expenses += expense
                    category_name = 'Travel'
                elif category == '3':
                    shopping_expenses += expense
                    category_name = 'Shopping'
                elif category == '4':
                    other_expenses += expense
                    category_name = 'Others'
                else:
                    print("Invalid category!")
                    continue
                total_expenses += expense
                add_to_history('Expense: Rs. '+ str(expense) + '| Category: ' + category_name)
                
                record = "Rs. " + str(expense) + " | Category: " + category_name

                expense_history.append(record)

                file = open("expense_history.txt", "a")
                file.write(record + "\n")
                file.close()

                print('Expense added successfully!')
                if total_expenses > pocket_money:
                    print('Warning: You have spent more than your pocket money!')
        elif choice == '2':
            balance = pocket_money - total_expenses
            print('\n--------Expense Summary-------')
            print('Pocket Money:', pocket_money)
            print("Food Expenses:", food_expenses)
            print("Travel Expenses:", travel_expenses)
            print("Shopping Expenses:", shopping_expenses)
            print("Other Expenses:", other_expenses)
            print('Total Expenses:', total_expenses)
            print('Remaining Balance:', balance)
        elif choice == '3':
            print('\nExpense History')
            if len(expense_history) == 0:
                print('No expenses recorded yet.')
            else:
                for item in expense_history:
                    print(item)
        elif choice == '4':
            break
        else:
            print('Invlid Choice!')

while True:

    print("\n1. Calculate")
    print('2. Scientific Calculator')
    print('3. Unit Converter')
    print("4. Equation Solver")
    print("5. Student Expense Tracker")
    print('6. View History')
    print("7. Clear History")
    print('8. Exit')

    menu = input("Enter your choice: ")

    if menu == "1":
        basic_calculator()
    elif menu == "2":
        scientific_calculator()
    elif menu == "3":
        unit_converter()
    elif menu == "4":
        equation_solver()
    elif menu == "5":
        expense_tracker()
    elif menu == "6":
        view_history()
    elif menu == "7":
        clear_history()
    elif menu == '8':
        print("Thank you for using PySolve!")
        break  
    else:
    
        print("Invalid operation")