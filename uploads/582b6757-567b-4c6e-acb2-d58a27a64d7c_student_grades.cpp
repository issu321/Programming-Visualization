#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <nlohmann/json.hpp>
using namespace std;
using json = nlohmann::json;

class Student {
private:
    string name;
    vector<int> grades;

public:
    Student(string n) : name(n) {}

    bool addGrade(int grade) {
        if (grade < 0 || grade > 100) return false;
        grades.push_back(grade);
        return true;
    }

    double getAverage() const {
        if (grades.empty()) return 0.0;
        double sum = 0;
        for (int g : grades) sum += g;
        return sum / grades.size();
    }

    char getLetterGrade() const {
        double avg = getAverage();
        if (avg >= 90) return 'A';
        if (avg >= 80) return 'B';
        if (avg >= 70) return 'C';
        if (avg >= 60) return 'D';
        return 'F';
    }

    string getName() const { return name; }
    vector<int> getGrades() const { return grades; }
};

class Classroom {
private:
    string className;
    vector<Student> students;

public:
    Classroom(string name) : className(name) {}

    void addStudent(const Student& s) {
        students.push_back(s);
    }

    double getClassAverage() const {
        if (students.empty()) return 0.0;
        double total = 0;
        for (const auto& s : students) {
            total += s.getAverage();
        }
        return total / students.size();
    }

    Student getTopStudent() const {
        if (students.empty()) throw runtime_error("No students");
        Student best = students[0];
        for (const auto& s : students) {
            if (s.getAverage() > best.getAverage()) {
                best = s;
            }
        }
        return best;
    }

    void saveToFile(const string& filepath) const {
        json data;
        data["class"] = className;
        for (const auto& s : students) {
            json student;
            student["name"] = s.getName();
            student["grades"] = s.getGrades();
            data["students"].push_back(student);
        }
        ofstream f(filepath);
        f << data.dump(2);
    }
};

int main() {
    Classroom classroom("Math 101");

    Student alice("Alice");
    alice.addGrade(85);
    alice.addGrade(92);
    alice.addGrade(78);
    classroom.addStudent(alice);

    Student bob("Bob");
    bob.addGrade(90);
    bob.addGrade(88);
    bob.addGrade(95);
    classroom.addStudent(bob);

    cout << "Class: " << classroom.getClassAverage() << endl;

    Student top = classroom.getTopStudent();
    cout << "Top: " << top.getName() << " (" << top.getAverage() << ")" << endl;

    classroom.saveToFile("grades.json");

    return 0;
}
