import csv
MAX_ASSIGNMENTS = 4 # max number of assignments we'll give a TA to grade

ta_names = ['Lily', 'Hannah']
grader_assignments = {}

# construct ta blocklist dict (key: ta name, value: list of blocklisted students)
blocklist_dict = {}
for ta in ta_names:
	filename = ta + '.csv'
	blocklisted_students = []
	with open(filename) as blocklist_csv:
		blocklist_reader = csv.reader(blocklist_csv, delimiter=',')
		for student_email in blocklist_reader:
			blocklisted_students.append(student_email[0])
	blocklist_dict[ta] = blocklisted_students
	grader_assignments[ta] = []


# read in student names
all_students = []
with open('FakeStudentNames.csv') as student_csv:
	students_reader = csv.reader(student_csv, delimiter=',')
	for student_email in students_reader:
		all_students.append(student_email[0])

remaining_tas = ta_names[:]
remaining_students = all_students[:]
for student in all_students:
	for ta in remaining_tas:
		if student not in blocklist_dict[ta]:
			grader_assignments[ta].append(student)
			if len(grader_assignments[ta]) >= MAX_ASSIGNMENTS:
				remaining_tas.remove(ta)
			remaining_students.remove(student)
			break

# FOR TESTING
for ta in ta_names:
	print(ta + "'s Assignments:")
	for student in grader_assignments[ta]:
		print(student)

print('UNASSIGNED STUDENTS:')
for student in remaining_students:
	print(student)