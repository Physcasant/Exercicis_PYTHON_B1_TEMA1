from datetime import datetime


def string_to_datetime(date_string: str, date_format: str = "%Y-%m-%d") -> datetime:
    """
    Converts a string to a datetime object using the specified format.

    Args:
        date_string (str): A string containing the date.
        date_format (str, optional): The format of the date string (default is '%Y-%m-%d').

    Returns:
        datetime: The resulting datetime object.
    """
    return datetime.strptime(date_string, date_format)


def datetime_to_string(date_time: datetime, date_format: str = "%Y-%m-%d") -> str:
    """
    Converts a datetime object to a string using the specified format.

    Args:
        date_time (datetime): The datetime object to convert.
        date_format (str, optional): The format of the resulting string (default is '%Y-%m-%d').

    Returns:
        str: The resulting string.
    """
    return date_time.strftime(date_format)
