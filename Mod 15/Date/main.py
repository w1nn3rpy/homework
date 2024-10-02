class Date:
    def __init__(self, day: int = 0, month:int = 0, year:int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'День: {self.day} Месяц: {self.month} Год: {self.year}'

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        dd, mm, yyyy = map(int, date.split('-'))
        return 0 < dd <= 31 and 0 < mm <= 12 and 0 < yyyy <= 9999

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        day, month, year = map(int, date.split('-'))
        dmy_object = cls(day, month, year)
        return dmy_object


date = Date.from_string('01-01-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))