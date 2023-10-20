import datetime as datetime

today = datetime.datetime.today()
epoch = datetime.datetime(1970, 1, 1)
delta = (today - epoch).total_seconds()

print(f"Seconds since {epoch.strftime('%B')} {epoch.day.__str__()}, \
    {epoch.year.__str__()}: {'{:,}'.format(delta)} \
    or {'{:.2e}'.format(delta)} in scientific notation")
print(today.strftime("%b"), today.day, today.year)
