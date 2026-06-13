from datetime import datetime, timezone

def extract_datetime(date, time):
    str_datetime = f"{date} {time}"
    dt = datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
    day = dt.strftime("%A")
    month = dt.strftime("%B")
    year = dt.year
    day_of_week = dt.isoweekday()
    day_of_the_month = dt.day
    week_of_year = dt.isocalendar()[1]
    day_of_year = dt.strftime("%j")
    
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

    data_meta_data={
        "datetime": dt.replace(microsecond=0),
        "day": day,
        "month":month,
        "year" :year,
        "day_of_week":day_of_week ,
        "day_of_the_month": day_of_the_month,
        "week_of_year": week_of_year,
        "day_of_year": day_of_year,
        }
    print(data_meta_data)
extract_datetime("2026-06-13", "11:43:12")