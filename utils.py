from datetime import datetime


def get_datetime_now():
    return datetime.utcnow()


def get_datetime_now_s():
    return datetime.utcnow().timestamp()


def get_datetime_now_h():
    return datetime.utcnow().strftime('%Hh%M\'')
