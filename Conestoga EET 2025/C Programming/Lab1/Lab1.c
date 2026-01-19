/*
Lab 1 - PROG1955
Matt Cunningham
9/12/2025
*/

#include <stdio.h>

int main(void)
{
    //======================================================================================
    // Question A
    //======================================================================================
    char aCharVariable = 0;
    short int aShortIntVariable = 0;
    int anIntVariable = 0;
    long long int aLongLongIntVariable = 0;
    float aFloatVariable = 0;
    double aDoubleVariable = 0;

    printf("Question A results:\n");
    printf("Size of char is %zd byte\n", sizeof(aCharVariable));
    printf("Size of short int is %zd bytes\n", sizeof(aShortIntVariable));
    printf("Size of int is %zd bytes\n", sizeof(anIntVariable));
    printf("Size of long long int is %zd bytes\n", sizeof(aLongLongIntVariable));
    printf("Size of float is %zd bytes\n", sizeof(aFloatVariable));
    printf("Size of double is %zd bytes\n", sizeof(aDoubleVariable));
    printf("\n");

    //======================================================================================
    // Question B
    //======================================================================================
    short int firstTwenty = 20;
    short int secondTwenty = 20;
    short int resultOfTwenties = firstTwenty * secondTwenty;

    printf("Question B result:\n");
    printf("20 times 20 is %hd\n", resultOfTwenties);
    printf("\n");

    //======================================================================================
    // Question C
    //======================================================================================

    short int firstTwoHundred = 200;
    short int secondTwoHundred = 200;
    short int resultOfTwoHundreds = firstTwoHundred * secondTwoHundred;

    printf("Question C result:\n");
    printf("200 times 200 is %hd\n", resultOfTwoHundreds);
    printf("Overflow.......\n");
    printf("\n");

    printf("Question C result, fixed:\n");
    int fixedResultOfTwoHundreds = firstTwoHundred * secondTwoHundred;
    printf("200 times 200 is actually %d\n", fixedResultOfTwoHundreds);
    /* fixed it by upgrading the result from a short int to an int, to fit the result of 40000, 
    as short int maxes out at 32,767 */
    printf("\n");

    //======================================================================================
    // Question D
    //======================================================================================
    int firstInput = 0;
    int secondInput = 0;

    printf("Question D inputs:\n");
    puts("Please enter an integer");
    scanf("%d", &firstInput);
    puts("Please enter another integer");
    scanf("%d", &secondInput);
    printf("\n");

    long long int sumOfInputs = firstInput + secondInput;
    long long int differenceOfInputs = firstInput - secondInput;
    long long int productOfInputs = firstInput * secondInput;
    long long int remainderOfInputs = firstInput % secondInput;
    long long int dividedInputs = firstInput / secondInput;

    printf("Question D results:\n");
    printf("%d + %d = %lld\n", firstInput, secondInput, sumOfInputs);
    printf("%d - %d = %lld\n", firstInput, secondInput, differenceOfInputs);
    printf("%d * %d = %lld\n", firstInput, secondInput, productOfInputs);
    printf("%d mod %d = %lld\n", firstInput, secondInput, remainderOfInputs);
    printf("%d / %d = %lld\n", firstInput, secondInput, dividedInputs);

    long double dividedInputsAsDouble = (double)firstInput / (double)secondInput;

    printf("%lf / %lf = %.3Lf\n", (double)firstInput, (double)secondInput, dividedInputsAsDouble);
    

    return 0;
}