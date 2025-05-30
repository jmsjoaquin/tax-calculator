from datetime import datetime


class SalaryTracker:
    def __init__(self, daily_rate: float, max_daily_hours: int = 8):
        if daily_rate <= 0:
            raise ValueError("Daily rate must be a positive number.")
        self.daily_rate = daily_rate
        self.max_daily_hours = max_daily_hours
        self.hourly_rate = self.daily_rate / self.max_daily_hours
        self.per_minute_rate = self.hourly_rate / 60

    def _calculate_daily_hours(self, time_in: str, time_out: str) -> float:
        in_time = datetime.strptime(time_in, "%H:%M")
        out_time = datetime.strptime(time_out, "%H:%M")
        worked_seconds = (out_time - in_time).total_seconds()
        hours = worked_seconds / 3600
        return min(hours, self.max_daily_hours)

    def compute_salary(self, time_entries: list[dict], month: int, year: int) -> dict:
        total_hours = 0
        valid_days = 0

        for entry in time_entries:
            entry_date = datetime.strptime(entry["date"], "%Y-%m-%d").date()
            if entry_date.year == year and entry_date.month == month:
                hours = self._calculate_daily_hours(entry["time_in"], entry["time_out"])
                total_hours += hours
                valid_days += 1

        gross = total_hours * self.hourly_rate

        return {
            "month": month,
            "year": year,
            "rate_type": "daily",
            "daily_rate": self.daily_rate,
            "hourly_rate": round(self.hourly_rate, 2),
            "per_minute_rate": round(self.per_minute_rate, 4),
            "valid_work_days": valid_days,
            "total_hours_worked": round(total_hours, 2),
            "gross_salary": round(gross, 2)
        }



# if __name__ == "__main__":
#     tracker = SalaryTracker(daily_rate=600)

#     entries = [
#         {"date": "2025-05-02", "time_in": "08:00", "time_out": "17:30"},
#         {"date": "2025-05-03", "time_in": "09:00", "time_out": "15:00"},
#         {"date": "2025-05-04", "time_in": "08:00", "time_out": "21:00"}
#     ]

#     result = tracker.compute_salary(entries, month=5, year=2025)
#     print(result)
