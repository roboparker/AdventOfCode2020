def get_group_any_yes_sum():
    yes = 0
    questions = {}
    data = open('input/day6.txt', 'r')
    for line in data:
        line = line.strip()
        if not line:
            questions = {}
        for char in line:
            if not (char in questions):
                questions[char] = True
                yes += 1
    data.close()
    return yes

def get_group_all_yes_sum():
    yes = 0
    group_questions = {}
    person_questions = {}
    new_group = True
    data = open('input/day6.txt', 'r')
    for line in data:
        line = line.strip()
        person_questions = {}
        if not line:
            yes += len(group_questions)
            group_questions = {}
            new_group = True
            continue
        for char in line:
            person_questions[char] = True
        if new_group:
            new_group = False
            group_questions = person_questions
        else:
            group_questions = set(group_questions).intersection(set(person_questions))
    yes += len(group_questions)
    data.close()
    return yes

def challenge_6_1():
    count = get_group_any_yes_sum()
    print(count, "group questions have been answered yes by anyone")


def challenge_6_2():
    count = get_group_all_yes_sum()
    print(count, "group questions have been answered yes by everyone")
