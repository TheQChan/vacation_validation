from datetime import timedelta


def validate_vacation(existing_employees_schedules, new_employees_schedules):

    # 1
    for period in new_employees_schedules.periods:
        if period.start_date >= period.end_date:
            print("Дата начала раньше конца")
            raise Exception

    # 4
    sum_vacation_day = sum(
        (p.end_date - p.start_date).days + 1 for p in new_employees_schedules.periods
    )
    if sum_vacation_day < 28:
        print("Общее число дней не должно быть меньше 28")
        raise Exception

    # 6
    vacation_flag = True
    for period in new_employees_schedules.periods:
        if (period.end_date - period.start_date).days + 1 == 14:
            vacation_flag = False
    if vacation_flag:
        print("В графике должен быть период в 14 дней")
        raise Exception
    # 3
    for period in new_employees_schedules.periods:
        weekends = 0
        current_date = period.start_date
        while current_date <= period.end_date:
            if current_date.weekday() >= 5:
                weekends += 1
            current_date += timedelta(days=1)

        if weekends < 2 and (period.end_date - period.start_date).days + 1 < 3:
            print("Нужно 2 выходных и 1 рабочий день минимум")
            raise Exception
