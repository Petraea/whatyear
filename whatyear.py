#!/usr/bin/env python
import argparse, datetime, calendar
parser = argparse.ArgumentParser()
parser.add_argument('-f','--future',action='store_true',help='Return future years instead of past ones.')
parser.add_argument("day_of_week")
parser.add_argument("day_of_month")
parser.add_argument("month")
args = parser.parse_args()

MAX_RESULTS = 10

REFERENCE_YEAR=1600 # Must be a leap year

weekdays=list(calendar.day_name)
months=list(calendar.month_name)

def name_selector(option, olist):
    '''Generically select the best matching text option from a list of texts.
Give a different error if you don't match any compared to matching too many.'''
    answers=set()
    for e in olist:
        for l in range(len(e),0,-1):
            short_e=e[:l]
            if short_e.lower() == option.lower():
                answers.add(e)
                break
    if len(answers)==0:
        raise ValueError('Option not found in list.')
    if len(answers)>1:
        raise IndexError('Option ambiguous. Could be %s ' % str(list(answers)))
    return list(answers)[0]

try:
    day_of_week=name_selector(args.day_of_week,weekdays)
except ValueError as e:
    print(str(e).replace('Option','Weekday'))
    exit(1)
except IndexError as e:
    print(str(e).replace('Option','Weekday'))
    exit(1)
dow = weekdays.index(day_of_week)

try:
    month=name_selector(args.month,months)
except ValueError as e:
    print(str(e).replace('Option','Month'))
    exit(1)
except IndexError as e:
    print(str(e).replace('Option','Month'))
    exit(1)
m = months.index(month)

max_dom=calendar.monthrange(REFERENCE_YEAR,m)[1]
try:
    day_of_month=int(args.day_of_month)
    if (day_of_month < 1) or (day_of_month > max_dom):
        raise ValueError
except ValueError:
    print('Month day not in range: [1,%s]'% max_dom)
    exit(1)
dom = day_of_month

matchingyears=[]
thisyear = datetime.date.today().year
if args.future:
    year_range = range(thisyear,thisyear+2000)
else:
    year_range = range(thisyear,0,-1)
for year in year_range:
    try:
        testdate = datetime.date(year,m,dom)
    except ValueError: #Only on 29th Feb
        continue
    if testdate.weekday() == dow:
        matchingyears.append(year)
    if len(matchingyears) >= MAX_RESULTS: break

print('For the day %s, %s %s:' % (day_of_week, day_of_month, month))
print('Matching years: %s ' % str(matchingyears))
