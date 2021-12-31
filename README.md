# SolarCalendar or IranianCalendar

This module allows you to output calendars like the Unix jcal program, and provides additional useful functions related
to the calendar. By default, these calendars have Saturday as the first day of the week, and Friday as the last (the
Iranian convention). Use setfirstweekday() to set the first day of the week to Monday (2) or to any other weekday.
Parameters that specify dates are given as integers. For related functionality, see also the datetime and time modules.


## Example
```python
>>> from solarcalendar import TextSolarCalendar
>>> calendar = TextSolarCalendar()
>>> print(a.formatmonth(1399, 10))

      Dey 1399
Sa Su Mo Tu We Th Fr
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30

>>> print(calendar.formatyear(1399))

                                  1399
     Farvardin                Ordibehesht                 Khordad
Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr
                   1             1  2  3  4  5                      1  2
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16
16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23
23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30
30 31                                               31
        Tir                      Mordad                  Shahrivar
Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr
    1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14
14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21
21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28
28 29 30 31               25 26 27 28 29 30 31      29 30 31
        Mehr                      Aban                      Azar
Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr
          1  2  3  4                      1  2       1  2  3  4  5  6  7
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       8  9 10 11 12 13 14
12 13 14 15 16 17 18      10 11 12 13 14 15 16      15 16 17 18 19 20 21
19 20 21 22 23 24 25      17 18 19 20 21 22 23      22 23 24 25 26 27 28
26 27 28 29 30            24 25 26 27 28 29 30      29 30
        Dey                      Bahman                    Esfand
Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr      Sa Su Mo Tu We Th Fr
       1  2  3  4  5                   1  2  3                         1
 6  7  8  9 10 11 12       4  5  6  7  8  9 10       2  3  4  5  6  7  8
13 14 15 16 17 18 19      11 12 13 14 15 16 17       9 10 11 12 13 14 15
20 21 22 23 24 25 26      18 19 20 21 22 23 24      16 17 18 19 20 21 22
27 28 29 30               25 26 27 28 29 30         23 24 25 26 27 28 29
                                                    30
```
## About SolarCalendar

From <a href=https://en.wikipedia.org/wiki/Solar_Hijri_calendar> wikipedia </a>, the Solar Hijri calendar (Persian: گاه‌شماری هجری خورشیدی, romanized: gāhshomāri-ye hejri-ye khorshidi; Pashto: لمريز
لېږدیز کلیز), also called the Iranian Hijri calendar or Shamsi Hijri calendar, and abbreviated as SH and, sometimes, HS,
is the official calendar of Iran and Afghanistan. It begins on the March equinox (Nowruz) as determined by astronomical
calculation for the Iran Standard Time meridian (52.5°E, UTC+03:30) and has years of 365 or 366 days.

Its determination of the start of each year is astronomically accurate year-to-year as opposed to the more fixed
Gregorian or Common Era calendar which, averaged out, has the same year length, achieving the same accuracy (a more
simply patterned calendar of 365 days for three consecutive years plus an extra day in the next year, save for
exceptions to the latter in three out of every four centuries). The start of the year and its number of days remain
fixed to one of the two equinoxes, the astronomically important days when day and night each have the same duration. It
results in less variability of all celestial bodies when comparing a specific calendar date from one year to others.

Each of the twelve months corresponds with a zodiac sign. The first six months have 31 days, the next five have 30 days,
and the last month has 29 days in usual years but 30 days in leap years. The Iranian New Year's Day always falls on the
March equinox.
