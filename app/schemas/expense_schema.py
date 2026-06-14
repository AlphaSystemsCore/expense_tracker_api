from pydantic import BaseModel
from datetime import date, time
from typing import Literal
from decimal import Decimal

class Expense_In(BaseModel):
    amount: Decimal
    categories: Literal['Tution & Fees', 'Accomodation', 'Food & Groceries', 'Transport', 'Book & Supplies', 'Clubs & Acitvities', 'Personal care', 'Entertainment', 'Communication', 'Miscelaneous']
    Date:date
    Time: time