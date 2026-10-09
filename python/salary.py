def analyze_salaries():
  print("--- Question 4: Employee Salary Analysis ---")
  raw_input = input("Enter employee salaries separated by spaces: ")
  salaries = [float(x) for x in raw_input.split()]
  if not salaries:
    print("No salaries entered.\n")
    return

  avg_salary = sum(salaries) / len(salaries)
  above_avg = [s for s in salaries if s > avg_salary]
  increased_salaries = [s * 1.10 for s in salaries]
  print(
      f"Average Salary: ₹{avg_salary:.2f}\nSalaries Above Average:"
      f" {above_avg}\n10% Increased Salaries: {increased_salaries}\n"
  )

if __name__ == ("__main__"):
  analyze_salaries()