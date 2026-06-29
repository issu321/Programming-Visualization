#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Student structure
struct Student {
    char name[50];
    int grades[10];
    int grade_count;
};

// Calculate average grade
float get_average(struct Student *s) {
    if (s->grade_count == 0) return 0.0;
    int sum = 0;
    for (int i = 0; i < s->grade_count; i++) {
        sum += s->grades[i];
    }
    return (float)sum / s->grade_count;
}

// Get letter grade
char get_letter_grade(float avg) {
    if (avg >= 90) return 'A';
    if (avg >= 80) return 'B';
    if (avg >= 70) return 'C';
    if (avg >= 60) return 'D';
    return 'F';
}

// Add grade to student
int add_grade(struct Student *s, int grade) {
    if (grade < 0 || grade > 100) return 0;
    if (s->grade_count >= 10) return 0;
    s->grades[s->grade_count] = grade;
    s->grade_count++;
    return 1;
}

int main() {
    struct Student alice;
    strcpy(alice.name, "Alice");
    alice.grade_count = 0;

    add_grade(&alice, 85);
    add_grade(&alice, 92);
    add_grade(&alice, 78);

    float avg = get_average(&alice);
    char letter = get_letter_grade(avg);

    printf("Student: %s\n", alice.name);
    printf("Average: %.1f\n", avg);
    printf("Grade: %c\n", letter);

    return 0;
}
