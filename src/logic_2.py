# Charging the battery for the ride home, from Lab 2. Each trip adds 10.
# TODO: this program has one bug. Fix it, then delete this line.

charge = 10
trips = 0
while charge < 40:
    print("Charging:", charge)
    trips = trips + 1
    charge + 10

print("Charging trips:", trips)
