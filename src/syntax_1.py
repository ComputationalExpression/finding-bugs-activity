# Waiting for dark, from Lab 3. The reading drops by 10 on every check.
# TODO: this program has one bug. Fix it, then delete this line.

reading = 50
checks = 0
while reading > 20
    reading = reading - 10
    checks = checks + 1

print("Checks until dark:", checks)
