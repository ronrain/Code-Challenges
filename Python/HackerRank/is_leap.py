def is_leap(year):
  leap = False
  if year % 4 == 0 and not year % 100 == 0:
        return True
  if year % 4 == 0 and year % 400 == 0:
        return True
  if year % 100 == 0 and not year % 400 == 0:
        return False
  return leap
print(is_leap(1992))
print(is_leap(2100))