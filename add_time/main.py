def add_time(start_time, duration, starting_day=None):
    # Parse start time
    start_time_parsed, am_pm = start_time.split(" ")
    start_time_hours, start_time_minutes = map(int, start_time_parsed.split((":")))

    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Total time
    total_minutes = start_time_minutes + duration_minutes
    total_hours = start_time_hours + duration_hours
    if total_minutes>60:
        total_minutes = total_minutes % 60
        total_hours += 1
    if am_pm == "PM":
        total_hours += 12

    return (total_hours, total_minutes)

print(add_time("3:30 PM", "33:35"))
