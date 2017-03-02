contestants = []
for i in range(1,6):
  total = sum(list(map(int, raw_input().split())))
  contestants.append((total, i))
contestants.sort(reverse=True)
print contestants[0][1], contestants[0][0]
