from datetime import datetime, timedelta

class Tools:

    def add_days(date_string, add_days):

        date_format = "%Y-%m-%d"
        current_date = datetime.strptime(date_string, date_format)
        next_day = current_date + timedelta(days=add_days)

        return next_day.strftime(date_format)
