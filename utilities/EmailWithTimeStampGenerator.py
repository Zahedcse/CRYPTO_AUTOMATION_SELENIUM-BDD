import random
import string
from datetime import datetime


def get_new_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "zahed" + time_stamp + "@gmail.com"


def generate_client_id(prefix="MPS", length=6):
    random_chars = ''.join(random.choices(string.ascii_letters, k=length))
    client_id = f"{prefix}{random_chars.isupper()}"
    return client_id
