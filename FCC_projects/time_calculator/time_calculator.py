def add_time(start, duration, day_of_week=''):

  # create a list to hold all the possible days in a week
  days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

  # a function that splits the time into a list of strings
  def time_of_day_split(time):
    return time.split()

  # a function loops through each item in the list and converts it to integers
  def time_split(time):
    return [int(i) for i in time.split(':')]

  # a simple dictionary to hold the time of day in AM or PM mapped to eeach other
  time_of_day_switch = {
    'AM': 'PM',
    'PM': 'AM'
  }

  
  time, init_period = time_of_day_split(start)
  init_hours, minutes = time_split(time)
  add_h, add_m = time_split(duration)

  hours = init_hours + add_h
  minutes += add_m
  days_later = 0
  dow, dlater, new_period = [''] * 3

  if minutes >= 59:
    hours += (minutes // 60)
    minutes %= 60

  if hours >= 24:
    days_later += hours // 24
    hours %= 24

  if (init_hours <= 11) and (hours > 11):
    new_period = time_of_day_switch[init_period]
    if (init_period, new_period) == ('PM', 'AM'):
      days_later += 1

    if hours > 12:
       hours %= 12

  if day_of_week:
    dayofweek_idx = (days.index(
    day_of_week.lower()) + days_later) % len(days)
    dow = f", {day_of_week[dayofweek_idx].title()}"

  if days_later == 1:
    dlater = " (next day)"
  elif days_later > 1:
    dlater = f" ({days_later} days later)"

    new_time = f"{hours}:{str(minutes).rjust(2, '0')} {new_period or init_period}{dow}{dlater}"

    return new_time


if __name__ == "__main__":
    actual = add_time("11:43 PM", "24:20", "tueSday")
    expected = "12:03 AM, Thursday (2 days later)"

    if actual != expected:
        print(actual)
    else:
        print("Well done!")




  # return new_time