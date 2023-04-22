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

    # Days later
    days_later = total_hours // 24
    if days_later == 1:
        days_later_str = f' (next day)'
    elif days_later > 1:
        days_later_str = f' ({days_later} days later)'
    else:
        days_later_str = ''

    # Define hours in AM PM period
    total_hours = total_hours % 24
    if total_hours > 12:
        total_hours = total_hours % 12
        am_pm = "PM"
    else:
        am_pm = "AM"

    # Add day of week if given
    if starting_day:
        starting_day = starting_day.lower()
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_weekday = weekdays.index(starting_day)
        end_weekday = (start_weekday + days_later) % 7
        day_of_week_str = f', {weekdays[end_weekday].capitalize()}'
    else:
        day_of_week_str = ''

    full_str = f'{total_minutes}:{total_minutes:02d} {am_pm}{day_of_week_str}{days_later_str}'
    return full_str
