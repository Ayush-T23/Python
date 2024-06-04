def calculate_bonus(salary, years_of_service):
    bonus = 0
    if years_of_service > 5:
        bonus = 0.05 * salary
    return bonus

salary = float(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the employee's years of service: "))

bonus_amount = calculate_bonus(salary, years_of_service)

print("Net bonus amount:", bonus_amount)

