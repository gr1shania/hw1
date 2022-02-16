duration = int(input("Duration:"))
day = (duration // (24 * 60 * 60))
hour = (duration // (60 * 60) - 24 * day)
minutes = (duration // 60 % 60)
seсonds = duration % 60
print("Ответ:", day, 'дн', hour, "час", minutes, "мин", seсonds, "сек")