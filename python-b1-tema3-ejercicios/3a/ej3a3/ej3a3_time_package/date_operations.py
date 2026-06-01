import datetime


def add_days(date: datetime, days: int) -> datetime:
    """
    Adds the specified number of days to a given date.

    Args:
        date (datetime): The initial datetime object.
        days (int): The number of days to add.

    Returns:
        datetime: A new datetime object with the specified number of days added.
    """
    return date + datetime.timedelta(days=days)


def middle_day_between_two_dates(
    initial_date: datetime, final_date: datetime
) -> datetime:
    """
    Calculates the middle day between two dates.

    Args:
        initial_date (datetime): The initial date.
        final_date (datetime): The final date.

    Returns:
        datetime: A date representing the middle day between the two input dates.
    """
    difference = final_date - initial_date
    middle_day = initial_date + datetime.timedelta(days=difference.days / 2)
    return middle_day
