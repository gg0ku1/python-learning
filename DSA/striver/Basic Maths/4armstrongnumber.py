original = 153

copy1 = original
copy2 = original

count = 0
while copy2 != 0:
    copy2 = copy2 // 10
    count += 1

total = 0
while copy1 != 0:
    lastdig = copy1 % 10
    copy1 = copy1 // 10
    total = total + lastdig ** count

if total == original:
    print(True)
else:
    print(False)



