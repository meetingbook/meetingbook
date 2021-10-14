from datetime import datetime, timedelta


class ConversionError(Exception):
    pass


class DateTime:
    def __init__(self, dt=None):
        self.datetime = dt

    def __str__(self):
        return str(self.datetime)

    def __call__(self, *args, **kwargs):
        return self.datetime

    def convert_to_datetime(self):
        try:
            self.datetime = datetime.fromisoformat(self.datetime[:-1])
            return self.datetime
        except Exception:
            raise ConversionError('set api_iso in ISO format for conversion')

    def convert_to_iso(self):
        try:
            self.datetime = self.datetime.isoformat()[:-3] + 'Z'
            return self.datetime
        except Exception:
            raise ConversionError('set datetime in datetime format for conversion')

    def set_utc_now(self):
        self.datetime = datetime.utcnow()

    def get_dt_for_link(self, validity_days=7, validity_hours=0):
        self.set_utc_now()
        self.datetime += timedelta(days=validity_days, hours=validity_hours)
        self.convert_to_iso()
        return self.datetime
