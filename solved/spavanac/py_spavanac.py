hours, minutes = map(int, raw_input().split())
if minutes >= 45:
  minutes -= 45
else:
  hours -= 1
  if hours == -1:
    hours = 23
  minutes += 15

print hours, minutes
