import pyperclip
import datetime

d = datetime.datetime.now()
d_date = d.strftime('%Y-%m-%dT%H:%M:%S-05:00')
pyperclip.copy(d_date)
