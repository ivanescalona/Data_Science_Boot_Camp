def get_date_from_unix(unix_time_stamp):
    year_unix = unix_time_stamp
    sec_reg_year = (365/1)*(24/1)*(3600/1)
    sec_leap_year = (366/1)*(24/1)*(3600/1)
    year = 1969
    
    while(year_unix > 0):
        year+=1
        month_unix = year_unix
        if (year % 4 != 0):
            year_unix = year_unix - sec_reg_year
        else:
            year_unix = year_unix - sec_leap_year
        
    
    
    month_days = month_unix//(3600*24)
    hours_min_sec = month_unix%(3600*24)
    leap = year % 4 == 0
    
    if (leap):
        month_days -= 1
    
    if (month_days < 31):
        month = 'Jan'
    elif (month_days < 59):
        month_days -= 30
        month = 'Feb'
    elif (month_days < 90):
        month_days -= 58
        month = 'Mar'
    elif (month_days < 120):
        month_days -= 89
        month = 'Apr'
    elif (month_days < 151):
        month_days -= 119
        month = 'May'
    elif (month_days < 181):
        month_days -= 150
        month = 'Jun'
    elif (month_days < 212):
        month_days -= 180
        month = 'Jul'
    elif (month_days < 243):
        month_days -= 211
        month = 'Aug'
    elif (month_days < 273):
        month_days -= 242
        month = 'Sep'
    elif (month_days < 304):
        month_days -= 272
        month = 'Oct'
    elif (month_days < 334):
        month_days -= 303
        month = 'Nov'
    else: 
        month_days -= 333
        month = 'Dec'
    if (leap and (month != 'Jan' or (month != 'Feb' and month_days != 28))):
        month_days -= 1
    
    day = int(month_days)
    
    hour = int(hours_min_sec//3600)
    minute = int((hours_min_sec%3600)//60)
    second = int((hours_min_sec%3600)%60)
    
    if hour < 10:
        hour = '0'+str(hour)
    if minute < 10:
        minute = '0'+str(minute)
    if second < 10:
        second = '0'+str(second)   
    
    date = f'{year}-{month}-{day} {hour}:{minute}:{second}'
    return date