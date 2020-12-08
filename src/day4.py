class Passport:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

    def is_valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

def basic_check():
    valid = 0
    passport = Passport()
    data = open('../input/day4.txt', 'r')
    for line, content in enumerate(data):
        content = content.strip()
        if not content:
            if passport.is_valid():
                valid += 1
            passport = Passport()
            continue
        parts = content.split()
        for part in parts:
            key, value = part.split(':', 1)
            if key == "byr":
                passport.byr = value
            elif key == "iyr":
                passport.iyr = value
            elif key == "eyr":
                passport.eyr = value
            elif key == "hgt":
                passport.hgt = value
            elif key == "hcl":
                passport.hcl = value
            elif key == "ecl":
                passport.ecl = value
            elif key == "pid":
                passport.pid = value
            elif key == "cid":
                passport.cid = value
    data.close()
    if passport.is_valid():
        valid += 1

print("Day 4, Challenge 1")
valid = basic_check()
print("valid", valid, "passports")