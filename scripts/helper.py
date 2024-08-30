import re

def clean_date(date_str):
    if isinstance(date_str, str):
        date_str = re.sub(r'([-+]\d{2}:\d{2})$', '', date_str)
        return date_str
    return date_str
