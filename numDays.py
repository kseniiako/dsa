def NumDaysBetween(year1, month1, day1, year2, month2, day2):
    
    num_days = 0
    start_year, start_mon = year1, month1
    
    while not((start_year == year2) and (start_mon == month2)):
        num_days += DaysInMonth(start_mon, start_year)
        if start_mon == 12:
            start_year += 1
            start_mon = 1
        else:
            start_mon +=1
            
    num_days -= day1
    num_days += day2
    
    return num_days

if __name__ == "__main__":
    print()