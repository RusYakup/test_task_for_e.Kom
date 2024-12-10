import re


def get_field_type(value: str) -> str:
    value = value.strip()
    if re.search(r'^\d{4}\.\d{2}\.\d{2}|\d{2}\.\d{2}\.\d{4}$', value):
        return "date"
    elif re.search(r'^7 \d{3} \d{3} \d{2} \d{2}$', value):
        return "phone"
    elif re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
        return "email"
    else:
        return "text"
