def student_teacher_ratio(number_of_students, number_of_teachers):
    print "The student-to-teacher ratio is %d." % (number_of_students / number_of_teachers)

student_teacher_ratio(100,5)

student_teacher_ratio(50 * 3, 24 / 4)

number_of_students = 600
number_of_teachers = 30
student_teacher_ratio(number_of_students, number_of_teachers)

student_teacher_ratio(number_of_students + 500, number_of_teachers - 3)

print student_teacher_ratio(3, 3)

print "%s" % student_teacher_ratio(80, 3)