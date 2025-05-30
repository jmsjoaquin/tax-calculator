class TaxCalculator:
    def __init__(self, tax_rate_percent: float, tax_type: str = "Withholding"):
        if tax_rate_percent < 0 or tax_rate_percent > 100:
            raise ValueError("Tax rate must be between 0 and 100.")
        self.tax_rate = tax_rate_percent
        self.tax_type = tax_type

    def compute_tax(self, gross: float) -> dict:
        tax_amount = gross * (self.tax_rate / 100)
        net_salary = gross - tax_amount

        return {
            "tax_type": self.tax_type,
            "tax_rate_percent": self.tax_rate,
            "gross_salary": round(gross, 2),
            "tax_deducted": round(tax_amount, 2),
            "net_salary": round(net_salary, 2)
        }
