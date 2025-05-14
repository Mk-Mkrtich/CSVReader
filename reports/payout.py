from typing import List, Dict
from collections import defaultdict


def generate_payout(data: List[Dict[str, str]]) -> None:
    grouped = defaultdict(list)

    for row in data:
        try:
            department = row["department"]
            grouped[department].append(row)
        except KeyError:
            continue

    for department, employees in grouped.items():
        print(f"{department}")
        print("  name".ljust(24) + "hours".rjust(6) + "  rate".rjust(6) + "  payout".rjust(8))
        total_hours = 0
        total_payout = 0

        for emp in employees:
            try:
                name = emp["name"]
                hours = float(emp["hours_worked"])
                rate = float(emp["hourly_rate"])
                payout = hours * rate
                total_hours += hours
                total_payout += payout

                print(f"  {'-' * 16} {name:<20}{int(hours):>6}{int(rate):>7}  ${int(payout):>6}")
            except (ValueError, KeyError):
                continue

        print(f"{'':>30}{int(total_hours):>6}  ${int(total_payout):>6}\n")
