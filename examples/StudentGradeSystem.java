import java.util.ArrayList;
import java.util.List;
import java.io.FileWriter;
import java.io.IOException;
import org.json.JSONObject;
import org.json.JSONArray;

public class StudentGradeSystem {

    static class Student {
        private String name;
        private List<Integer> grades;

        public Student(String name) {
            this.name = name;
            this.grades = new ArrayList<>();
        }

        public boolean addGrade(int grade) {
            if (grade < 0 || grade > 100) return false;
            grades.add(grade);
            return true;
        }

        public double getAverage() {
            if (grades.isEmpty()) return 0.0;
            int sum = 0;
            for (int g : grades) sum += g;
            return (double) sum / grades.size();
        }

        public char getLetterGrade() {
            double avg = getAverage();
            if (avg >= 90) return 'A';
            if (avg >= 80) return 'B';
            if (avg >= 70) return 'C';
            if (avg >= 60) return 'D';
            return 'F';
        }

        public String getName() { return name; }
        public List<Integer> getGrades() { return grades; }
    }

    static class Classroom {
        private String className;
        private List<Student> students;

        public Classroom(String name) {
            this.className = name;
            this.students = new ArrayList<>();
        }

        public void addStudent(Student s) {
            students.add(s);
        }

        public double getClassAverage() {
            if (students.isEmpty()) return 0.0;
            double total = 0;
            for (Student s : students) {
                total += s.getAverage();
            }
            return total / students.size();
        }

        public Student getTopStudent() {
            if (students.isEmpty()) return null;
            Student best = students.get(0);
            for (Student s : students) {
                if (s.getAverage() > best.getAverage()) {
                    best = s;
                }
            }
            return best;
        }

        public void saveToFile(String filepath) throws IOException {
            JSONObject data = new JSONObject();
            data.put("class", className);
            JSONArray arr = new JSONArray();
            for (Student s : students) {
                JSONObject st = new JSONObject();
                st.put("name", s.getName());
                st.put("grades", s.getGrades());
                arr.put(st);
            }
            data.put("students", arr);
            FileWriter fw = new FileWriter(filepath);
            fw.write(data.toString(2));
            fw.close();
        }
    }

    public static void main(String[] args) {
        Classroom classroom = new Classroom("Math 101");

        Student alice = new Student("Alice");
        alice.addGrade(85);
        alice.addGrade(92);
        alice.addGrade(78);
        classroom.addStudent(alice);

        Student bob = new Student("Bob");
        bob.addGrade(90);
        bob.addGrade(88);
        bob.addGrade(95);
        classroom.addStudent(bob);

        System.out.println("Class: " + classroom.className);
        System.out.println("Class Average: " + classroom.getClassAverage());

        Student top = classroom.getTopStudent();
        if (top != null) {
            System.out.println("Top Student: " + top.getName() + " (" + top.getAverage() + ")");
        }

        try {
            classroom.saveToFile("grades.json");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
