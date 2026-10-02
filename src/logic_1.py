# The chase from Lab 4, with print standing in for the lights.
# It should run one lap for every round.
# TODO: this program has one bug. Fix it, then delete this line.

rounds = 3
laps = 0
for lap in range(1, rounds):
    print("Round", lap)
    laps = laps + 1

print("Chase rounds:", laps)
