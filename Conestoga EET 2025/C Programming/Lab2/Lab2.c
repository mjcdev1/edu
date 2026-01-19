
/*
Lab 2 - PROG1955
Matt Cunningham
9/19/2025
*/

#include <stdio.h>

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

    int smallestInt = firstInput;

    if (smallestInt > secondInput) {
        smallestInt = secondInput;
    }

    if (smallestInt > thirdInput) {
        smallestInt = thirdInput;
    }

    if (smallestInt > fourthInput) {
        smallestInt = fourthInput;
    }
 
    printf("\n");

    printf("The smallest int is %d\n", smallestInt);
    if (smallestInt % 3 == 0) {
        printf("%d is a multiple of 3!", smallestInt);
    }
    else {
        printf("%d is not a multiple of 3 :(", smallestInt);
    }

    printf("\n");

    //======================================================================================
    // Question B
    //======================================================================================
    
    float aCanOfSoda = 1.5;
    double usersDepositAmount = 0;
    double usersAddlDepositAmount = 0;

    printf("\n");
    printf("=======================================================================================\n");
    puts("\nWelcome To Your Local Soda Pop Vending Machine, Produced by the C Language Company.\n");
    puts("Please insert your money. A can of soda costs 1.50:");
    scanf("%lf", &usersDepositAmount);

    double usersShortAmount = aCanOfSoda - usersDepositAmount;

    if (usersDepositAmount < aCanOfSoda) {
        puts("\nUh oh, you didn't enter enough money to pay for your soda.\n");
        printf("Please make an additional deposit of at least %.2lf\n", usersShortAmount);
        scanf("%lf", &usersAddlDepositAmount);
        printf("\n");

        usersDepositAmount += usersAddlDepositAmount;
    }

    if (usersDepositAmount >= aCanOfSoda) {
        double usersChangeAmount = usersDepositAmount - aCanOfSoda;
        printf("\nThank you for your purchase, enjoy your soda.\n");
        if (usersChangeAmount == 0.00) {
            printf("You have no change.\n");
        }
        else {
            printf("Your change is %.2lf\n", usersChangeAmount);
        }
    }
    else {
        printf("You didn't add enough money. You've been denied from purchasing this soda.\n");
    }


    return 0;
}