import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

x = datetime.datetime.now()
print(x)
print(x.year)

# ************** Creating Date Objects **************

# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.

# Create a date object:
data = datetime.datetime(1987, 11, 30)
print(data)
# ************** The strftime() Method **************

# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

# Display the name of the month:
print(x.strftime('%B'))

# Display the name of the day:
print(x.strftime('%A'))


data_formatada = data.strftime('%A, %d de %B de %Y')
print(data_formatada)

# Local version of date and time
print(x.strftime('%c'))