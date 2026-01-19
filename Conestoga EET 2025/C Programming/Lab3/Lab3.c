/*
Lab 3 - PROG1955
Matt Cunningham
9/26/2025
*/

#include <stdio.h>

int insertLineSpace();
int insertLineSpace() {
    printf("\n");
}

int main()
{

    //======================================================================================
    // Question A
    //======================================================================================

    int firstInput = 0;
    int secondInput = 0;

    puts("Please enter an integer");
    scanf("%d", &firstInput);

    puts("Please enter another integer");
    scanf("%d", &secondInput);

    insertLineSpace();

    int count = 0;
    int total = 0;
    double average = 0;

    for (int i = firstInput + 1; i < secondInput; i++) {
        if (i % 2 == 1) {
            total += i;
            count += 1;
        }
    }

    insertLineSpace();

    if (count <= 0) {
        printf("No even numbers exist between %d and %d.\n", firstInput, secondInput);
    }
    else {
        printf("Total sum of all even integers between %d and %d: %d\n", firstInput, secondInput, total);
        printf("Total count of all even integers between %d and %d: %d\n", firstInput, secondInput, count);
        average = (double)total / count;
        printf("Average: %.2lf", average);
    }

    //======================================================================================
    // Question B
    //======================================================================================

    float aCanOfSoda = 2.5;
    double usersDepositAmount = 0;
    double totalAmountDeposited = 0;

    printf("\n");
    printf("=======================================================================================\n");
    puts("\nWelcome To Your Local Soda Pop Vending Machine, Produced by the C Language Company.\n");
    puts("Please insert your money. A can of soda costs 2.50:");
    scanf("%lf", &usersDepositAmount);

    totalAmountDeposited += usersDepositAmount;

    while (totalAmountDeposited < aCanOfSoda) {
        double amountLeftToPay = 0;
        amountLeftToPay = aCanOfSoda - totalAmountDeposited;
        insertLineSpace();
        printf("Uh oh, you didn't insert enough money to pay for your soda. You must pay %.2lf more for your soda.\n", amountLeftToPay);
        puts("Please enter more money:");
        scanf("%lf", &usersDepositAmount);
        totalAmountDeposited += usersDepositAmount;
    }

    insertLineSpace();
    printf("Thank you for your purchase, enjoy your soda!\n");

    double usersChangeAmount = 0;
    usersChangeAmount = totalAmountDeposited - aCanOfSoda;
    
    if (usersChangeAmount <= 0.0) {
        printf("You have no change");
    }
    else {
        printf("Your change is %.2lf", usersChangeAmount);
    }

    insertLineSpace();
    
    return 0;
}
