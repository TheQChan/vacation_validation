from models import Employee
from validator import validate_vacation

if __name__ == "__main__":
    try:
        existing = [
            Employee(
                1,
                [
                    {"start_date": "01.06.2025", "end_date": "15.06.2025"},
                    {"start_date": "01.08.2025", "end_date": "14.08.2025"},
                ],
            ),
            Employee(
                2, [{"start_date": "01.07.2025", "end_date": "28.07.2025"}]
            ),
        ]

        new_schedule = Employee(
            3,
            [
                {
                    "start_date": "10.06.2025",
                    "end_date": "05.06.2025",
                },
                {"start_date": "01.07.2025", "end_date": "10.07.2025"},
                {
                    "start_date": "05.07.2025",
                    "end_date": "15.07.2025",
                },
                {
                    "start_date": "25.07.2025",
                    "end_date": "30.07.2025",
                },
            ],
        )
        validate_vacation(existing, new_schedule)
    except Exception as e:
        print(f"Ошибка валидации. {e}")
