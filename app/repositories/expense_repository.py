from app.db.db_connection import get_cur

def create_expense_repo(user_id:str, amount:int, expense_cat_id, time_metadata: dict):
    with get_cur() as cur:
        cur.execute(
            """
            INSERT INTO time_metadata
            (datetime, day, month, year, day_of_week, day_of_month, week_of_year, day_of_year)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s) RETURNING time_id
            """, ( time_metadata.get("datetime"),time_metadata.get("day"),time_metadata.get("month"), time_metadata.get("year"), time_metadata.get("day_of_week"), time_metadata.get("day_of_the_month"), time_metadata.get("week_of_year"),time_metadata.get("day_of_year") ))
        time_id = cur.fetchone()

        cur.execute("""
            INSERT INTO expenses
            (amount, expense_cat_id, user_id, time_id) 
            VALUES(%s,%s, %s, %s)""",
            (amount, expense_cat_id, user_id, time_id))

        
        
