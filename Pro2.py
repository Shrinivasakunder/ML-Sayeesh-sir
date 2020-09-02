from datetime import date
f = date(2020, 8, 17)
l = date(2020, 9, 2)
delta = l - f
print(f'Number of days between {f} and {l} are: {delta.days}')
