from typing import List


def get_average_grades(all_grades: dict[str: List[int]]) -> int:
    result = []
    for key, value in all_grades.items():
        result.append(sum(value) / len(value))
    average_grades = sum(result) / len(result)
    return average_grades


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __gt__(self, other):
        average_grades_self = get_average_grades(self.grades)
        average_grades_other = get_average_grades(other.grades)

        if isinstance(other, Student):
            if average_grades_self > average_grades_other:
                return f'Cредние оценки студента {self.name} больше, чем студента {other.name}'
        else:
            return f'Типы сравниваемых объектов отличаются!'

    def __lt__(self, other):
        average_grades_self = get_average_grades(self.grades)
        average_grades_other = get_average_grades(other.grades)
        if isinstance(other, Student):
            if average_grades_self < average_grades_other:
                return f'Cредние оценки студента {self.name} больше, чем студента {other.name}'
        else:
            return f'Типы сравниваемых объектов отличаются!'

    def __eq__(self, other):
        average_grades_self = get_average_grades(self.grades)
        average_grades_other = get_average_grades(other.grades)
        if isinstance(other, Student):
            if average_grades_self == average_grades_other:
                return f'Cредние оценки студента {self.name} равны оценкам студента {other.name}'
        else:
            return f'Типы сравниваемых объектов отличаются!'

    def __str__(self):
        average_grades = get_average_grades(self.grades)
        # result = []
        # for key, value in self.grades.items():
        #     result.append(sum(value)/len(value))
        # average_grades = sum(result)/len(result)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(average_grades, 2)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __gt__(self, other):
        average_grades_self = get_average_grades(self.grades)
        average_grades_other = get_average_grades(other.grades)

        if isinstance(other, Lecturer):
            if average_grades_self > average_grades_other:
                return f'Cредние оценки лектора {self.name} больше, чем лектора {other.name}'
        else:
            return f'Типы сравниваемых объектов отличаются!'

    def __lt__(self, other):
        average_grades_self = get_average_grades(self.grades)
        average_grades_other = get_average_grades(other.grades)
        if isinstance(other, Lecturer):
            if average_grades_self < average_grades_other:
                return f'Cредние оценки лектора {self.name} больше, чем лектора {other.name}'
        else:
            return f'Типы сравниваемых объектов отличаются!'

    def __eq__(self, other):
        average_grades_self = get_average_grades(self.grades)
        average_grades_other = get_average_grades(other.grades)
        if isinstance(other, Lecturer):
            if average_grades_self == average_grades_other:
                return f'Cредние оценки лектора {self.name} равны оценкам лектора {other.name}'
        else:
            return f'Типы сравниваемых объектов отличаются!'

    def __str__(self):
        average_grades = get_average_grades(self.grades)
        # result = []
        # for key, value in self.grades.items():
        #     result.append(sum(value)/len(value))
        # average_grades = sum(result)/len(result)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(average_grades, 2)}\n'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_student = Student('Molly', 'Gwins', 'your_gender')
cool_student.courses_in_progress += ['Git']
cool_student.courses_in_progress += ['Python']
cool_student.courses_in_progress += ['Django']
cool_student.finished_courses += ['Введение в программирование']

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Git']

second_reviewer = Reviewer('Karl', 'Stone')
second_reviewer.courses_attached += ['Git']
second_reviewer.courses_attached += ['Django']

first_lecturer = Lecturer('Spam', 'Eggs')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['Git']

second_lecturer = Lecturer('Lama', 'Alabama')
second_lecturer.courses_attached += ['Django']
second_lecturer.courses_attached += ['Python']

first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Git', 9)
first_reviewer.rate_hw(cool_student, 'Python', 10)

second_reviewer.rate_hw(best_student, 'Django', 8)
second_reviewer.rate_hw(cool_student, 'Git', 10)
second_reviewer.rate_hw(cool_student, 'Django', 7)

best_student.rate_lecturer(first_lecturer, 'Python', 10)
cool_student.rate_lecturer(first_lecturer, 'Git', 8)
# print(best_student.grades)
# print(cool_student.grades)
print(first_lecturer.grades)
print(second_lecturer.grades)


# print(first_reviewer)
# print(first_lecturer)
# print(best_student)
# print(cool_student)


def get_average_students_grade_course(students_list: List[Student], course: str):
    result = []
    for student in students_list:
        if course in student.grades:
            for grade in student.grades[course]:
                result.append(grade)

    average_course_grade = sum(result) / len(result)
    return f'Средняя оценка студентов по курсу {course} составляет {average_course_grade}'


def get_average_lecturers_grade_course(lecturers_list: List[Lecturer], course: str):
    result = []
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            for grade in lecturer.grades[course]:
                result.append(grade)
#
#
    average_course_grade = sum(result) / len(result)
    return f'Средняя оценка лекторов по курсу {course} составляет {average_course_grade}'


print(get_average_students_grade_course([best_student, cool_student], 'Git'))
print(get_average_lecturers_grade_course([first_lecturer, second_lecturer], 'Git'))
