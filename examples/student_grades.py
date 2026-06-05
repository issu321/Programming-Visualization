"""Student grade management system."""
import json
import statistics

class Student:
    """Represents a student with grades."""

    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades or []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        return 'F'

class Classroom:
    """Manages multiple students."""

    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_class_average(self):
        if not self.students:
            return 0
        total = 0
        for student in self.students:
            total += student.get_average()
        return total / len(self.students)

    def get_top_student(self):
        if not self.students:
            return None
        best = self.students[0]
        for student in self.students:
            if student.get_average() > best.get_average():
                best = student
        return best

    def save_to_file(self, filepath):
        data = {
            'class': self.class_name,
            'students': [
                {'name': s.name, 'grades': s.grades}
                for s in self.students
            ]
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

def main():
    classroom = Classroom("Math 101")

    alice = Student("Alice")
    alice.add_grade(85)
    alice.add_grade(92)
    alice.add_grade(78)
    classroom.add_student(alice)

    bob = Student("Bob")
    bob.add_grade(90)
    bob.add_grade(88)
    bob.add_grade(95)
    classroom.add_student(bob)

    print(f"Class: {classroom.class_name}")
    print(f"Class Average: {classroom.get_class_average():.1f}")

    top = classroom.get_top_student()
    if top:
        print(f"Top Student: {top.name} ({top.get_average():.1f})")

    classroom.save_to_file("grades.json")

if __name__ == '__main__':
    main()
