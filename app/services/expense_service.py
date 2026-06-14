from datetime import datetime, timezone
from app.repositories.expense_repository import create_expense_repo
from app.exceptions.expense_exceptions import DateTimeExtractionError
def extract_datetime(date, time):
    try:
        str_datetime = f"{date} {time}"
        def str_parse(s:str):
            for fmt in ("%Y-%m-%d %H:%M:%S.%f%z",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y-%m-%d %H:%M"
            ):
                try:
                    return datetime.strptime(s, fmt)
                except ValueError:
                    continue
            raise ValueError(f"Unsupported datetime format {s}")

        dt = str_parse(str_datetime)
        day = dt.strftime("%A")
        month = dt.strftime("%B")
        year = dt.year
        day_of_week = dt.isoweekday()
        day_of_the_month = dt.day
        week_of_year = dt.isocalendar()[1]
        day_of_year = dt.strftime("%j")
    except DateTimeExtractionError:
        raise
  
    datetime_metadata= {
                        "datetime": dt.replace(microsecond=0),
                        "day": day,
                        "month":month,
                        "year" :int(year),
                        "day_of_week":int(day_of_week) ,
                        "day_of_the_month": int(day_of_the_month),
                        "week_of_year": int(week_of_year),
                        "day_of_year": int(day_of_year),
                        }

    return datetime_metadata 



def create_expense_service(user_id, amount, category,date, time):
    category_id_look_up = {
        'Tution & Fees':1, 
        'Accomodation':2, 
        'Food & Groceries':3, 
        'Transport':4, 
        'Book & Supplies':5, 
        'Clubs & Acitvities':6, 
        'Personal care':7, 
        'Entertainment':8, 
        'Communication':9, 
        'Miscelaneous':10
        }
    try:
        datetime_metadata = extract_datetime(date, time)

        create_expense_repo(user_id, amount, category_id_look_up.get(category), datetime_metadata)
    except Exception as e:
        print(e)
        raise

    

