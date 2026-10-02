# Every third flash is long, from Lab 3.
# TODO: this program has one bug. Fix it, then delete this line.

pattern = 7
for flash in range(1, pattern + 1):
    if flash % 3 == 0:
        long_flashes = long_flashes + 1

print("Long flashes:", long_flashes)
