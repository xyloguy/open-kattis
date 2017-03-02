out = ''
for char in raw_input():
  if len(out) > 0:
    if out[-1] != char:
      out += char
  else:
    out = char
print out
