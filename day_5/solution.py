def read_input():
    clean_lines = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    for line in range(len(lines)):
        if line == len(lines) - 1:
            clean_lines.append(lines[line])
        else:
            clean_lines.append(lines[line][:-1])
    return clean_lines


def separate_rules_and_updates(lines):
    rules = []
    updates = []
    for line in lines:
        if "|" in line:
            rules.append(line)
        elif "," in line:
            updates.append(line)
    return rules, updates


def find_rules_for_update(update, rules):
    part_rules = []
    final_rules = []
    for i in range(len(update)):
        for rule in rules:
            if update[i] == rule[:2]:
                part_rules.append(rule)
    for pr in part_rules:
        if pr[3:] in update:
            final_rules.append(pr)
    return final_rules


def verify_update(update, rules):
    rule_counter = 0
    confirmed_rule_counter = 0
    rules = find_rules_for_update(update, rules)
    for i in range(len(update)):
        for rule in rules:
            if update[i] == rule[:2]:
                rule_counter += 1
                if rule[3:] in update[i+1:]:
                    confirmed_rule_counter += 1
    return rule_counter == confirmed_rule_counter


def find_middle_number(update):
    mid = float(len(update)) / 2
    if mid % 2 != 0:
        return update[int(mid - 0.5)]
    else:
        return update[update[int(mid)], update[int(mid - 1)]]


def verify_updates_and_count(updates, rules):
    outcomes = []
    for update in updates:
        update = list(update.split(','))
        if verify_update(update, rules):
            outcomes.append(int(find_middle_number(update)))
    return sum(outcomes)


def get_faulty_updates(updates, rules):
    faulty_updates = []
    for update in updates:
        update = list(update.split(','))
        if not verify_update(update, rules):
            faulty_updates.append(update)
    return faulty_updates


def get_incorrect_rules(update, rules):
    incorrect_rules = []
    rules = find_rules_for_update(update, rules)
    for i in range(len(update)):
        for rule in rules:
            if update[i] == rule[:2]:
                if rule[3:] not in update[i+1:]:
                    incorrect_rules.append(rule)
    return incorrect_rules


def correct_faulty_update(update, rules):
    for rule in rules:
        temp_index = update.index(rule[3:])
        update[update.index(rule[:2])] = rule[3:]
        update[temp_index] = rule[:2]
    return update

def correct_all_updates(updates, rules):
    corrected_updates = []
    for update in updates:
        while not verify_update(update, rules):
            ir = get_incorrect_rules(update, rules)
            update = correct_faulty_update(update, ir)
        corrected_updates.append(update)
    return corrected_updates


def verify_corrected_updates_and_count(updates, rules):
    outcomes = []
    for update in updates:
        if verify_update(update, rules):
            outcomes.append(int(find_middle_number(update)))
    return sum(outcomes)

cl = read_input()
r, u = separate_rules_and_updates(cl)
first_answer = verify_updates_and_count(u, r)
fu = get_faulty_updates(u, r)
cu = correct_all_updates(fu, r)
second_answer = verify_corrected_updates_and_count(cu, r)
