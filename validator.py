from models import ValidationError


def validate_vacation(existing_employees_schedules, new_employees_schedules):
    # 2
    for existing_employee in existing_employees_schedules:
        for existing_period in existing_employee.periods:
            for new_period in new_employees_schedules.periods:
                if existing_period.overlaps_with(new_period):
                    raise ValidationError(
                        f"Отпуск пересекается с отпуском сотрудника {existing_employee.id} "
                        f"({existing_period.start_date.strftime('%d.%m.%Y')}-"
                        f"{existing_period.end_date.strftime('%d.%m.%Y')})"
                    )

    new_employees_schedules._validate_periods()
