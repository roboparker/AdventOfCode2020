import re

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


    def display(self):
        print("byr", self.byr, "iyr", self.iyr, "eyr", self.eyr)
        print("hgt", self.hgt, "hcl", self.hcl, "ecl", self.ecl)
        print("pid", self.pid, "cid", self.cid)


    def is_valid(self, validate_fields=False):
        has_required_fields = self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid
        if not validate_fields:
            return has_required_fields
        elif not has_required_fields:
            return False
        if int(self.byr) < 1920 or int(self.byr) > 2002:
            return False
        if int(self.iyr) < 2010 or int(self.iyr) > 2020:
            return False
        if int(self.eyr) < 2020 or int(self.eyr) > 2030:
            return False
        if len(self.hgt) < 4:
            return False
        height_unit = self.hgt[-2:]
        height = int(self.hgt[:-2])
        if height_unit != "cm" and height_unit != "in":
            return False
        if (height_unit == "cm" and (height < 150 or height > 193)) or (height_unit == "in" and (height < 59 or height > 76)):
            return False
        if not re.search("^#[0-9a-f]{6}$", self.hcl):
            return False
        if not re.search("^(amb|blu|brn|gry|grn|hzl|oth){1}$", self.ecl):
            return False
        if not re.search("^[0-9]{9}$", self.pid):
            return False
        return True

def basic_check(validate_fields=False):
    valid = 0
    passport = Passport()
    data = open('input/day4.txt', 'r')
    for line, content in enumerate(data):
        content = content.strip()
        if not content:
            if passport.is_valid(validate_fields):
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
    if passport.is_valid(validate_fields):
        valid += 1
    return valid

def challenge_4_1():
    valid = basic_check()
    print(valid, "valid passports")

def challenge_4_2():
    valid = basic_check(True)
    print(valid, "valid passports")