import locale as _mod_locale

ABDAY_1 = 14
ABDAY_2 = 15
ABDAY_3 = 16
ABDAY_4 = 17
ABDAY_5 = 18
ABDAY_6 = 19
ABDAY_7 = 20
ABMON_1 = 33
ABMON_10 = 42
ABMON_11 = 43
ABMON_12 = 44
ABMON_2 = 34
ABMON_3 = 35
ABMON_4 = 36
ABMON_5 = 37
ABMON_6 = 38
ABMON_7 = 39
ABMON_8 = 40
ABMON_9 = 41
ALT_DIGITS = 49
AM_STR = 5
CHAR_MAX = 127
CODESET = 0
CRNCYSTR = 56
DAY_1 = 7
DAY_2 = 8
DAY_3 = 9
DAY_4 = 10
DAY_5 = 11
DAY_6 = 12
DAY_7 = 13
D_FMT = 2
D_T_FMT = 1
ERA = 45
ERA_D_FMT = 46
ERA_D_T_FMT = 47
ERA_T_FMT = 48
Error = _mod_locale.Error
LC_ALL = 0
LC_COLLATE = 1
LC_CTYPE = 2
LC_MESSAGES = 6
LC_MONETARY = 3
LC_NUMERIC = 4
LC_TIME = 5
MON_1 = 21
MON_10 = 30
MON_11 = 31
MON_12 = 32
MON_2 = 22
MON_3 = 23
MON_4 = 24
MON_5 = 25
MON_6 = 26
MON_7 = 27
MON_8 = 28
MON_9 = 29
NOEXPR = 53
PM_STR = 6
RADIXCHAR = 50
THOUSEP = 51
T_FMT = 3
T_FMT_AMPM = 4
YESEXPR = 52
__doc__ = 'Support for POSIX locales.'
__name__ = '_locale'
__package__ = ''
def localeconv():
    '() -> dict. Returns numeric and monetary locale-specific parameters.'
    return dict()

def nl_langinfo(key):
    'nl_langinfo(key) -> string\nReturn the value for the locale information associated with key.'
    return ''

def setlocale():
    '(integer,string=None) -> string. Activates/queries locale processing.'
    return ''

def strcoll():
    'string,string -> int. Compares two strings according to the locale.'
    return 1

def strxfrm(string):
    'strxfrm(string) -> string.\n\nReturn a string that can be used as a key for locale-aware comparisons.'
    return ''

