from datetime import datetime, timedelta


class ConversionError(Exception):
    pass


class DateTime:
    def __init__(self, dt=None):
        self.datetime = dt
        self.js_iso_8601 = None

    def __str__(self):
        return str(self.datetime)

    def __call__(self, *args, **kwargs):
        return self.datetime

    def convert_to_datetime(self, js_iso_8601):
        try:
            self.datetime = datetime.fromisoformat(js_iso_8601[:-1])
            return self.datetime
        except Exception:
            raise ConversionError(f'{js_iso_8601}must be in format: "YYYY-MM-DDTHH:mm:ss.sssZ"')

    def convert_to_iso(self):
        try:
            self.js_iso_8601 = self.datetime.isoformat()[:-3] + 'Z'
            return self.js_iso_8601
        except Exception:
            raise ConversionError('set datetime in datetime format for conversion')

    def set_utc_now(self):
        self.datetime = datetime.utcnow()

    def utc_plus_delta(self, days=0, hours=0):
        self.set_utc_now()
        self.datetime += timedelta(days=days, hours=hours)
        return self.convert_to_iso()
