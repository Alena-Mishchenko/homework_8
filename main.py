from datetime import datetime, timedelta,date
from collections import defaultdict
def get_birthdays_per_week(users):
  
    current_date = date.today()
    next_week_start = current_date + timedelta(days=7)

    birthdays_to_greet = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []   
    }
    greeting_list = defaultdict(list)
    
    for user in users:
        name = user.get("name")
        birthday_date = user.get("birthday")

        if name and birthday_date:       
            if birthday_date.year != current_date.year:
                birthday_date = birthday_date.replace(year=current_date.year)

            if (current_date <= birthday_date < next_week_start) \
                or (current_date <= birthday_date.replace(year=current_date.year+1) < next_week_start):
                day_of_week = birthday_date.strftime("%A")
                if day_of_week in birthdays_to_greet:
                    greeting_list[day_of_week].append(name)
                elif day_of_week in ("Saturday", "Sunday"):
                    greeting_list["Monday"].append(name)

    return greeting_list
