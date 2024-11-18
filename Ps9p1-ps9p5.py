# Problem 1: Compute Extended Price with Discount
def comp_ext_price(qty, unit_price):
    ext_price = qty * unit_price
    discount = ext_price * 0.10 if ext_price > 10000 else 0
    return ext_price - discount


# Problem 2: Compute Batting Average
def comp_batting_avg(hits, at_bats):
    return hits / at_bats if at_bats > 0 else 0


# Problem 3: Compute Miles Per Gallon
def comp_mpg(miles, gallons):
    return miles / gallons if gallons > 0 else 0


# Problem 4: Compute Gross Pay
def get_pay_rate(job_code):
    rates = {'L': 25, 'A': 30, 'J': 50}
    return rates.get(job_code.upper(), 0)


# Problem 5: Compute Tuition Owed
def comp_tuition(credit_hours, district_code):
    rate = 250 if district_code.upper() == 'I' else 550
    return credit_hours * rate


# Problem 6: Compute Reward Points
def comp_rewards(points, code):
    multiplier = {'C': 2, 'X': 3}
    return points * multiplier.get(code.upper(), 1.5)


# Problem 7: Perform Operations
def perform_operation(num1, num2, op_code):
    if op_code.upper() == 'A':
        return num1 + num2
    elif op_code.upper() == 'S':
        return num1 - num2
    elif op_code.upper() == 'M':
        return num1 * num2
    elif op_code.upper() == 'D':
        return num1 / num2 if num2 != 0 else -999
    else:
        return None


# Problem 8: String Case Transformation
def transform_string(original):
    if original.islower():
        return original.upper()
    else:
        return original.lower()


# Main Program
def main():
    while True:
        print("\nSelect an option:")
        print("1. Extended Price Calculation")
        print("2. Batting Average Calculation")
        print("3. Miles Per Gallon Calculation")
        print("4. Gross Pay Calculation")
        print("5. Tuition Calculation")
        print("6. Reward Points Calculation")
        print("7. Perform Operation")
        print("8. String Transformation")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            total_ext_price = 0
            while True:
                qty = float(input("Enter quantity (Ctrl+Z to stop): "))
                price = float(input("Enter price: "))
                ext_price = comp_ext_price(qty, price)
                print(
                    f"Quantity: {qty}, Price: {price}, Extended Price: {ext_price}"
                )
                total_ext_price += ext_price
                cont = input("Continue? (Yes/No): ")
                if cont.lower() != 'yes':
                    break
            print(f"Total Extended Price: {total_ext_price}")

        elif choice == '2':
            player_count = 0
            while True:
                last_name = input(
                    "Enter player's last name (Ctrl+Z to stop): ")
                hits = int(input("Enter number of hits: "))
                at_bats = int(input("Enter number of at-bats: "))
                avg = comp_batting_avg(hits, at_bats)
                print(f"Player: {last_name}, Batting Average: {avg}")
                player_count += 1
                cont = input("Continue? (Yes/No): ")
                if cont.lower() != 'yes':
                    break
            print(f"Total Players: {player_count}")

        elif choice == '3':
            trip_count = 0
            while True:
                city = input("Enter destination city (Ctrl+Z to stop): ")
                miles = float(input("Enter miles travelled: "))
                gallons = float(input("Enter gallons used: "))
                mpg = comp_mpg(miles, gallons)
                print(f"City: {city}, Miles: {miles}, MPG: {mpg}")
                trip_count += 1
                cont = input("Continue? (Yes/No): ")
                if cont.lower() != 'yes':
                    break
            print(f"Total Trips: {trip_count}")

        elif choice == '4':
            total_gross_pay = 0
            while True:
                last_name = input(
                    "Enter employee's last name (Ctrl+Z to stop): ")
                job_code = input("Enter job code (L/A/J): ")
                hours = float(input("Enter hours worked: "))
                rate = get_pay_rate(job_code)
                gross_pay = hours * rate
                if hours > 40:
                    gross_pay += (hours - 40) * rate * 0.5
                print(f"Employee: {last_name}, Gross Pay: {gross_pay}")
                total_gross_pay += gross_pay
                cont = input("Continue? (Yes/No): ")
                if cont.lower() != 'yes':
                    break
            print(f"Total Gross Pay: {total_gross_pay}")

        elif choice == '5':
            total_tuition = 0
            while True:
                last_name = input(
                    "Enter student's last name (Ctrl+Z to stop): ")
                credit_hours = int(input("Enter credit hours: "))
                district_code = input("Enter district code (I/O): ")
                tuition = comp_tuition(credit_hours, district_code)
                print(f"Student: {last_name}, Tuition: {tuition}")
                total_tuition += tuition
                cont = input("Continue? (Yes/No): ")
                if cont.lower() != 'yes':
                    break
            print(f"Total Tuition Owed: {total_tuition}")

        elif choice == '6':
            while True:
                points = int(input("Enter points (Ctrl+Z to stop): "))
                code = input("Enter redemption code (C/X/Other): ")
                rewards = comp_rewards(points, code)
                print(f"Points: {points}, Code: {code}, Rewards: {rewards}")
                cont = input("Continue? (Yes/No): ")
                if cont.lower() != 'yes':
                    break

        elif choice == '7':
            while True:
                num1 = float(input("Enter first number (Ctrl+Z to stop): "))
                num2 = float(input("Enter second number: "))
                op_code = input("Enter operation code (A/S/M/D): ")
                result = perform_operation(num1, num2, op_code)
                if result == -999:
                    print("Cannot divide by zero.")
                print(f"Result: {result}")
                cont = input("Continue? (Yes/No): ")
                if cont.lower() != 'yes':
                    break

        elif choice == '8':
            while True:
                string = input("Enter a string (Ctrl+Z to stop): ")
                new_string = transform_string(string)
                print(f"Original: {string}, Transformed: {new_string}")
                cont = input("Continue? (Yes/No): ")
                if cont.lower() != 'yes':
                    break

        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
