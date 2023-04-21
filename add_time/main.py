def add_time(start_time, duration, starting_day=None):
    # Parse start time
    start_time_parsed, am_pm = start_time.split(" ")
    start_time_hours, start_time_minutes = map(int, start_time_parsed.split((":")))

    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    return (start_time_hours, start_time_minutes)

print(add_time("3:30 PM", "2:12"))
