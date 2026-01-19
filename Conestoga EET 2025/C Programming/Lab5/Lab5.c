/*
Lab 5 - PROG1955
Matt Cunningham
10/13/2025
*/

#include <stdio.h>

int insertLineSpace(void);
int insertLineSpace(void) {
    printf("\n");
}

float GradePoints(char grade);
float GradePoints(char grade) {
    switch (grade) {
    case 'A':
        return 4.0;
    case 'B':
        return 3.0;
    case 'C':
        return 2.0;
    case 'D':
        return 1.0;
    case 'F':
        return 0.0;
    default:
        return 0.0;
    }
}

float Gpa(char grades[], char hours[], int arrLength);
float Gpa(char grades[], char hours[], int arrLength) {
    float points = 0;
    float totalHours = 0;
    float result = 0;

    for (int i = 0; i < arrLength; i++) {
        float grade = GradePoints(grades[i]);
        float h = (float)(hours[i] - '0');
        points += grade * h;
        totalHours += h;
    }

    result = points / totalHours;

    return result;
}

int main()
{
    char grades[5];
    char hours[5];
    int arrLength = 5;

    puts("Welcome to the C Company Grading Software\n");

    for (int i = 0; i < arrLength; i++) {
        printf("Please enter a grade for course number %d: ", i + 1);
        scanf(" %c", &grades[i]);
    }

    insertLineSpace();

    for (int i = 0; i < arrLength; i++) {
        printf("Please enter the hours for course number %d: ", i + 1);
        scanf(" %c", &hours[i]);
    }

    insertLineSpace();

    float gpa = Gpa(grades, hours, arrLength);
    printf("Your GPA is: %.2f\n", gpa);

    return 0;
}
