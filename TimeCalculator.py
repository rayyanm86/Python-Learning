def add_time(start, duration,day=None):
    days = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
    start_t, starting_status = start.split()
    duration_hrs, duration_mins = duration.split(':')
    start_hrs, start_mins = start_t.split(':')
    start_hrs = int(start_hrs)
    start_mins = int(start_mins)
    duration_hrs = int(duration_hrs)
    duration_mins = int(duration_mins)

    if start_hrs == 12 and starting_status == 'AM':
        start_hrs = 0
    elif start_hrs != 12 and starting_status == 'PM':
        start_hrs = start_hrs + 12
    mins = start_mins + duration_mins
    extra_hrs = mins // 60
    mins = mins % 60

    hrs = start_hrs + duration_hrs + extra_hrs
    extra_day = hrs // 24
    hrs = hrs % 24

    if hrs == 0:
        hrs = 12
        status = 'AM'
    elif hrs > 12:
        hrs = hrs - 12
        status = 'PM'
    elif hrs == 12:
        status = 'PM'
    else:
        status = 'AM'
    new_time = f'{hrs}:{mins:02d} {status}'
    if day!=None:
        day = day.capitalize()
        pos = days.index(day)
        index = (pos+extra_day)%7
        day = days[index]
        new_time += f", {day}"
    if extra_day == 1:
        new_time += " (next day)"
    elif extra_day > 1:
        new_time += f" ({extra_day} days later)"

    return new_time


print(add_time('11:59 PM', '24:05'))
