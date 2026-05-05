diesel = 48
km = 0

while diesel > 0:
    km = km + 100
    diesel = diesel - 3
    if diesel % 7 == 0:
        diesel = 1

print(km)
#1600
