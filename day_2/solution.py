def read_input():
    reports = []
    with open('input.txt') as file:
        lines = file.readlines()
    for line in lines:
        reports.append(line[:-1])
    return reports


def reports_to_list(reports):
    new_reports = []
    for report in reports:
        new_reports.append(list(map(int, report.split(' '))))
    return new_reports


def check_asc_or_desc(reports):
    asc_or_desc_reports = []
    for report in reports:
        if check_asc_or_desc_single(report):
            asc_or_desc_reports.append(report)
    return asc_or_desc_reports


def check_asc_or_desc_single(report):
    return all(report[i] < report[i + 1] for i in range(len(report) - 1)) or all(
        report[i] > report[i + 1] for i in range(len(report) - 1))

def check_is_safe_report(report):
    return all(-3 <= (report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1))


def get_safe_reports(reports):
    safe_reports = []
    for report in reports:
        if check_is_safe_report(report):
            safe_reports.append(report)
    return safe_reports

def get_safe_reports_with_removal(reports):
    safe_reports = []
    for report in reports:
        for level_position in range(len(report)):
            temp_report = report[:level_position] + report[level_position + 1:]
            if check_asc_or_desc_single(temp_report):
                if check_is_safe_report(temp_report):
                    safe_reports.append(report)
                    break
    return safe_reports

r = read_input()
r = reports_to_list(r)
asc_desc_r = check_asc_or_desc(r)
safe_r = get_safe_reports(asc_desc_r)
first_answer = len(safe_r)

safe_r_after_removal = get_safe_reports_with_removal(r)
second_answer = len(safe_r_after_removal)
