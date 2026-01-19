/*
Assignment 1 - PROG1955
Matt Cunningham
11/28/2025
*/

#include <stdio.h>

void countFunction();
void countFunction() {
    static int count = 0;
    count++;

    printf("We have called this function %d times\n",  count);
}

unsigned int reverseBinary(unsigned int num);
unsigned int reverseBinary(unsigned int num) {
    unsigned int flip = 0;

    for (int i = 0; i < 32; i++) {
        flip = flip << 1;
        unsigned int bit = num & 1;
        flip = flip | bit;
        num = num >> 1;
    }

    return flip;
}

unsigned int printBinary(unsigned int num); 
unsigned int printBinary(unsigned int num) {
    for (int i = 31; i >= 0; i--) {
        unsigned int binary = (num >> i) & 1;
        printf("%u", binary);
        
        if (i % 8 == 0 && i != 0) {
            printf(" ");
        }
    }
}

int main(void)
{
    //======================================================================================
    // Question A
    //======================================================================================

    countFunction();
    countFunction();
    countFunction();
    countFunction();
    countFunction();
    countFunction();
    countFunction();
    countFunction();

    //======================================================================================
    // Question B
    //======================================================================================

    unsigned int flipThis;

    printf("\nPlease enter an unsigned interger: ");
    scanf("%u", &flipThis);

    printf("\nYou entered %u with bits: ", flipThis);
    printBinary(flipThis);

    unsigned int flippedResult = reverseBinary(flipThis);

    printf("\nThe reversed-bit number is: %u with bits: ", flippedResult);
    printBinary(flippedResult);
    puts("\n");
    
    return 0;
}
