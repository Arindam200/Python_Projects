def add_time(start, duration, day = 'false'):

  list_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  new_time = ''
  total_day = 0
  
  time = start.split()
  meridiem = time[1]
  split_start = time[0].split(':')
  hour_start = int(split_start[0])
  minute_start = int(split_start[1])
  
  split_duration = duration.split(':')
  hour_duration = int(split_duration[0])
  minute_duration = int(split_duration[1])

  if meridiem == 'PM':
    hour_start += 12
  
  minute_res = minute_start + minute_duration

  if minute_res >= 60:
    minute_res -= 60
    hour_duration += 1

  hour_res = hour_start + hour_duration

  if hour_res >= 24:
    total_day = hour_res // 24
    hour_res = hour_res % 24

  if hour_res == 0:
    hour_res = 12
    meridiem = 'AM'
  elif hour_res == 12:
    meridiem = 'PM'
  elif hour_res > 12:
    hour_res -= 12
    meridiem = 'PM'
  else:
    meridiem = 'AM'

  hour_res = str(hour_res)
  minute_res = str(minute_res)

  if len(minute_res) == 1:
    minute_res = ''.join(('0', minute_res))

  if day == 'false':
    new_time += hour_res + ':' + minute_res + ' ' + meridiem
  else:
    day = day.lower().title()
    index_day = list_day.index(day)
    sum_day = index_day + total_day
    if sum_day > 6:
      index_day = (sum_day % 7)
    else:
      index_day = sum_day
      
    new_time += hour_res + ':' + minute_res + ' ' + meridiem + ', ' + list_day[index_day]

  if total_day > 0:
    if total_day == 1:
      new_time += ' (next day)'
    else:
      new_time += ' (' + str(total_day) + ' days later)'
  
  return new_time