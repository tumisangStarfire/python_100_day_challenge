from pydantic import BaseModel
from typing import Optional


class SMS(BaseModel):
    message = str
    phone_number = str
    message = str
    status_code = int
    retry_attempts = int
    date_sent = str
