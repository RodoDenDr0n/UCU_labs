"""CALENDAR"""
import calendar

def semester_calendar(output_type, year, first_month, last_month):
    """
    This function returns calendar in "txt" ot "html" format
    >>> print('Hello World!')
    Hello World!
    """
    row = ""
    if output_type == "txt" or output_type == "html":
        pass
    else:
        return
    if output_type == "txt":
        for i in range((last_month - first_month) + 1):
            row += calendar.month(year, first_month)
            first_month += 1
    elif output_type == "html":
        for i in range(last_month - first_month + 1):
            cal_html = calendar.HTMLCalendar(0)
            row += cal_html.formatmonth(year, first_month + i)
    return row

print(semester_calendar("txt", 2021, 10, 12))
