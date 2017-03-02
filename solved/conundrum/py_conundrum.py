count = 0
string = raw_input().upper()
for i in range(len(string)):
  if i%3 == 0 and string[i] != 'P':
    count += 1

  if i%3 == 1 and string[i] != 'E':
    count += 1

  if i%3 == 2 and string[i] != 'R':
    count += 1
print count
