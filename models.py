from datetime import datetime, timedelta


class ValidationError(Exception):
    pass


class VacationPeriod:
    def __init__(self, start_date, end_date):
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y").date()
        self.end_date = datetime.strptime(end_date, "%d.%m.%Y").date()
        self._validate_period()

    def _validate_period(self):
        # 1
        if self.start_date >= self.end_date:
            raise ValidationError(
                "Дата начала отпуска должна быть раньше даты окончания"
            )

        # 3
        weekends = 0
        current_date = self.start_date
        while current_date <= self.end_date:
            if current_date.weekday() >= 5:
                weekends += 1
            current_date += timedelta(days=1)

        if weekends < 2 and (self.end_date - self.start_date).days + 1 < 3:
            raise ValidationError(
                "Период отпуска должен включать минимум 2 выходных и 1 рабочий день"
            )

    def overlaps_with(self, other_period):
        """Проверяет пересекается ли период с другим периодом"""
        return not (
            self.end_date < other_period.start_date
            or self.start_date > other_period.end_date
        )


class Employee:
    def __init__(self, id, periods):
        self.id = id
        self.periods = [
            VacationPeriod(period["start_date"], period["end_date"])
            for period in periods
        ]
        self._validate_periods()

    def _validate_periods(self):
        # 5
        for i in range(len(self.periods)):
            for j in range(i + 1, len(self.periods)):
                if self.periods[i].overlaps_with(self.periods[j]):
                    raise ValidationError(
                        "Периоды отпуска не должны пересекаться друг с другом"
                    )

        # 4
        sum_vacation_day = sum(
            (p.end_date - p.start_date).days + 1 for p in self.periods
        )
        if sum_vacation_day < 28:
            raise ValidationError(
                "Общее число дней отпуска не должно быть меньше 28"
            )

        # 6
        if not any(
            (period.end_date - period.start_date).days + 1 == 14
            for period in self.periods
        ):
            raise ValidationError("В графике должен быть период в 14 дней")
