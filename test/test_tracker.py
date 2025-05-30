from tracker_salary.salary_tracker import SalaryTracker
from calculate_tax.tax_calculator import TaxCalculator

# 1. Initialize Salary Tracker
tracker = SalaryTracker(daily_rate=600)

# 2. Provide sample attendance entries
entries = [
    {"date": "2025-05-02", "time_in": "08:00", "time_out": "17:30"},
    {"date": "2025-05-03", "time_in": "09:00", "time_out": "15:00"},
    {"date": "2025-05-04", "time_in": "08:00", "time_out": "21:00"},
]

# 3. Compute salary for May 2025
salary_result = tracker.compute_salary(entries, month=5, year=2025)

# 4. Initialize Tax Calculator
taxer = TaxCalculator(tax_rate_percent=5, tax_type="Withholding")

# 5. Compute tax from gross salary
tax_result = taxer.compute_tax(salary_result["gross_salary"])

# 6. Combine both results
final_result = {**salary_result, **tax_result}

# 7. Output the result
print("🧾 Final Salary + Tax Result")
print(final_result)
