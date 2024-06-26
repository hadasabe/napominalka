import datetime as dt

a = dt.date.fromisoformat('2024-06-26')
b = dt.date.today()
c = dt.datetime.now().time()


print(a == b, c)

