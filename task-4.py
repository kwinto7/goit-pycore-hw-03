from datetime import datetime, timedelta

def get_upcoming_birthdays(users_list):
    today_date = datetime.today().date()
    next_week_start = today_date + timedelta(days=(7-today_date.weekday()))
    next_week_end = next_week_start + timedelta(days=6)

    greetings = []

    for user in users_list:
        user_birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birthday_this_year = user_birthday_date.replace(year=today_date.year)
        
        if user_birthday_this_year < today_date: # will greet next year
            user_birthday_this_year = user_birthday_this_year.replace(year = today_date.year + 1)
        
        elif next_week_start <= user_birthday_this_year <= next_week_end: # birthday next week
            greeting_date = user_birthday_this_year
            if greeting_date.weekday() in (5, 6):# weekend check
                greeting_date += timedelta(days=(7 - greeting_date.weekday()))# will greet on monday
                        
            greetings.append({
                "name": user["name"],
                "greeting_date": greeting_date
            })
    return greetings

users = [
    {"name": "John Doe", "birthday": "1985.06.18"},
    {"name": "Jane Smith", "birthday": "1990.06.21"}
]

for user in get_upcoming_birthdays(users):
    print(f"{user['name']} sholud be congradulated {user['greeting_date']}")




