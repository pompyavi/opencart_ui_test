import time


def get_random_gmail():
    timestamp = time.time().__floor__()
    return f'automation{timestamp}@gmail.com'



