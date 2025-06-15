from datetime import datetime

def get_days_from_today(date):
    try:
        specific_date = datetime.strptime(date, "%Y-%m-%d")
        today_date = datetime.today()
        time_delta = today_date - specific_date
        return  f"Від сьогодні до введеної дати {time_delta.days} днів" 
    except ValueError:
        return "Введіть дату в форматі РРРР-ММ-ДД (наприклад, 2021-10-09)."

print(get_days_from_today("2020-10-09"))