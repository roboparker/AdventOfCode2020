import src.day1 as d1
import src.day2 as d2
import src.day3 as d3
import src.day4 as d4
import src.day5 as d5
import src.day6 as d6

print("=" * 50)
print("Advent of code")
print("=" * 50)

day = int(input("Choose day: "))
while day < 1 or day > 31:
    day = int(input("Invalid day. Choose a day (1-31): "))
challenge = int(input("Choose challenge: "))
while challenge != 1 and challenge != 2:
    day = int(input("Invalid challenge. Choose a challenge (1-2): "))

print("Running")

if day == 1 and challenge == 1:
    d1.challenge_1_1()
elif day == 1 and challenge == 2:
    d1.challenge_1_2()
elif day == 2 and challenge == 1:
    d2.challenge_2_1()
elif day == 2 and challenge == 2:
    d2.challenge_2_2()
elif day == 3 and challenge == 1:
    d3.challenge_3_1()
elif day == 3 and challenge == 2:
    d3.challenge_3_2()
elif day == 4 and challenge == 1:
    d4.challenge_4_1()
elif day == 4 and challenge == 2:
    d4.challenge_4_2()
elif day == 5 and challenge == 1:
    d5.challenge_5_1()
elif day == 5 and challenge == 2:
    d5.challenge_5_2()
elif day == 6 and challenge == 1:
    d6.challenge_6_1()
elif day == 6 and challenge == 2:
    d6.challenge_6_2()

print("=" * 50)