/*
Lab 4 - PROG1955
Matt Cunningham
10/06/2025
*/

#include <stdio.h>

int insertLineSpace(void);
int insertLineSpace(void) {
    printf("\n");
}

int smallest(int num1, int num2, int num3, int num4);
int smallest(int num1, int num2, int num3, int num4) {
    int smallestInt = num1;
    
    if (smallestInt > num2) {
        smallestInt = num2;
    }

    if (smallestInt > num3) {
        smallestInt = num3;
    }

    if (smallestInt > num4) {
        smallestInt = num4;
    }

    return smallestInt;
}

int isMultipleOf3(int number);
int isMultipleOf3(int number) {

    if (number % 3 == 0) {
        return 1;
    }
    else {
        return 0;
    }
}

double oddAverage(int a, int b);
double oddAverage(int a, int b) {
    long long int count = 0;
    long long int total = 0;
    double average = 0;

    for (long long int i = a + 1; i < b; i++) {
        if (i % 2 != 0) {
            total += i;
            count += 1;
        }
    }

    average = (double)total / (double)count;
    return average;
}




int main(void)
{

    //======================================================================================
    // Question A
    //======================================================================================

    int firstInput = 0;
    int secondInput = 0;
    int thirdInput = 0;
    int fourthInput = 0;

    puts("Please enter an integer");
    scanf("%d", &firstInput);
    puts("Please enter another integer");
    scanf("%d", &secondInput);
    puts("Please enter a third integer");
    scanf("%d", &thirdInput);
    puts("Please enter a fourth integer");
    scanf("%d", &fourthInput);

    insertLineSpace();


    int smallestIntResult = smallest(firstInput, secondInput, thirdInput, fourthInput);
    printf("The smallest int is %d\n", smallestIntResult);

    int isMultipleOf3Result = isMultipleOf3(smallestIntResult);
    if (isMultipleOf3Result == 1) {
        printf("%d is a multiple of 3!\n", smallestIntResult);
    }
    else if (isMultipleOf3Result == 0) {
        printf("%d is not a multiple of 3 :(\n", smallestIntResult);
    }

    insertLineSpace();

    //======================================================================================
    // Question B
    //======================================================================================

    printf("=======================================================================================\n");

    insertLineSpace();

    int fifthInput = 0;
    int sixthInput = 0;

    puts("Please enter an integer");
    scanf("%d", &fifthInput);

    puts("Please enter another integer");
    scanf("%d", &sixthInput);

    insertLineSpace();

    double oddOverageResult = oddAverage(fifthInput, sixthInput);
    printf("The average of all odd numbers between %d and %d is %.2lf\n", fifthInput, sixthInput, oddOverageResult);

    return 0;
}

