def Output(hr, mn, Meridiem, number_of_days, day):
    days = ''
    if number_of_days == 0:
        days = ''
    elif number_of_days == 1:
        days = ' (next day)'
    elif number_of_days > 1:
        days = f' ({number_of_days} days later)'
    if day:
        day = f', {day}'
    return f'{hr}:{str(mn).zfill(2)} {Meridiem}{day}{days}'

def add_time(start, duration, day=''):
    
    # Declaring Variables
    #Variables from input:
    start_arr = start.replace(" ",":").split(':')
    start_arr_int = [int(start_arr[0]), int(start_arr[1]), start_arr[2]]
    if start_arr[2] == "PM":  start_arr_int[0] += 12
    duration_arr = duration.split(':')
    duration_arr_int = [int(duration_arr[0]), int(duration_arr[1])]
    
    daysInWeek = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    #Variables for output:
    Meridiem = "AM"
    day_result = ""
    #Time and Days Calculation:
    mn_result = start_arr_int[1] + duration_arr_int[1]
    mn_result_adj = mn_result % 60
    hr_result = start_arr_int[0] + duration_arr_int[0] + mn_result // 60
    hr_result_adj = hr_result % 24
    number_of_days = hr_result // 24
    if hr_result_adj >=12:
        Meridiem = "PM"
    if hr_result_adj > 12:
        hr_result_adj -= 12
    if hr_result_adj == 0:
        hr_result_adj = 12
    if day:
        day_lower_cap = day.lower()
        index_day = daysInWeek.index(day.lower())
        index_day_adj =  (index_day + number_of_days) % 7
        day_result = daysInWeek[index_day_adj].capitalize()
    return Output(hr_result_adj, mn_result_adj, Meridiem, number_of_days, day_result)

print(add_time('11:59 PM', '48:05', 'Friday'))
