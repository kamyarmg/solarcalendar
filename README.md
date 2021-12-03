# SolarHijriCalendar or IranianCalendar

This module allows you to output calendars like the Unix jcal program, and provides additional useful functions related
to the calendar. By default, these calendars have Saturday as the first day of the week, and Friday as the last (the
Iranian convention). Use setfirstweekday() to set the first day of the week to Monday (2) or to any other weekday.
Parameters that specify dates are given as integers. For related functionality, see also the datetime and time modules.


## Example
```python
    from solar_hijri_calendar import SolarHijriCalendar
    calendar = SolarHijriCalendar()
    print(a.formatmonth(1399, 10))

      Dey 1399
Sa Su Mo Tu We Th Fr
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30

```
## About Solar Hijri Calendar

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
