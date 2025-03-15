import pandas as pd
from datetime import datetime, timedelta

title = 'Jazz Show'

today = datetime.today().date()

days_until_tuesday = (1 - today.weekday()) % 7

date = str(today + timedelta(days=days_until_tuesday))
date = date + ' 20:00'
date = datetime.strptime(date, '%Y-%m-%d %H:%M')

events = pd.DataFrame({'title': [title], 'date': [date]})