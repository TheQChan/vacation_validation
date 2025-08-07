from datetime import datetime


class VacationPeriod:
    def __init__(self, start_date, end_date):
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y").date()
        self.end_date = datetime.strptime(end_date, "%d.%m.%Y").date()


class Employee:
    def __init__(self, id, periods):
        self.id = id
        self.periods = [
            VacationPeriod(period["start_date"], period["end_date"])
            for period in periods
        ]
