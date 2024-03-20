def check_employee_bonus(years_in_service, office):
    # Check years in service condition
    if years_in_service >= 10:
        # Check office condition
        if office == "IT":
            bonus = 10000
        elif office == "Accountant":
            bonus = 12000
        elif office == "Human Resources":
            bonus = 15000
        else:
            print("Invalid office. Please enter a valid office (IT, Accountant, Human Resources).")
            return
    else:
        # Check office condition
        if office == "IT":
            bonus = 5000
        elif office == "Accountant":
            bonus = 6000
        elif office == "Human Resources":
            bonus = 7500
        else:
            print("Invalid office. Please enter a valid office (IT, Accountant, Human Resources).")
            return

    print("Employee is eligible for a bonus of", bonus, "bonus.")

# Prompt for employee's years in service
while True:
    years_in_service = input("Enter the number of years in service: ")
    if years_in_service.isdigit():
        years_in_service = int(years_in_service)
        break
    else:
        print("Invalid input. Please enter a numeric value for years in service.")

# Prompt for employee's office
while True:
    office = input("Enter the office (IT, Accountant, Human Resources): ")
    if office in ["IT", "Accountant", "Human Resources"]:
        break

# Call the function to check employee bonus eligibility
check_employee_bonus(years_in_service, office)
