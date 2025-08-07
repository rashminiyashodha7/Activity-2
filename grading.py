
while True:
    user_input = input("Enter your marks (0 - 100): ")

    try:
        marks = float(user_input)

        if 0 <= marks <= 100:
            if marks >= 75:
                grade = 'A'
            elif marks >= 65:
                grade = 'B'
            elif marks >= 55:
                grade = 'C'
            elif marks >= 35:
                grade = 'S'
            else:
                grade = 'F'
            print(f"Your grade is: {grade}")
            break 
        else:
            print("Marks must be between 0 and 100. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
