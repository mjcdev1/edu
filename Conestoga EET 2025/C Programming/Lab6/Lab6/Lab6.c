/*
Lab 6 - PROG1955
Matt Cunningham
11/7/2025
*/

#include <stdio.h>

int insertLineSpace();
int insertLineSpace() {
    printf("\n");
}

int minMax(int a, int b, int c, int *min, int *max);
int minMax(int a, int b, int c, int* min, int* max) {
    *min = a;
    *max = a;

    if (b < *min) *min = b;
    if (c < *min) *min = c;

    if (b > *max) *max = b;
    if (c > *max) *max = c;
}

int swapInts(int *first, int *second);
int swapInts(int *first, int *second) {
    int swap = 0;

    swap = *first;
    *first = *second;
    *second = swap;
}

int main(void)
{
    //======================================================================================
    // Question A
    //======================================================================================
    int a = 0;
    int b = 0;
    int c = 0;
    int min = 0;
    int max = 0;

    puts("Please enter an integer:");
    scanf("%d", &a);

    puts("\nPlease enter another integer:");
    scanf("%d", &b);

    puts("\nPlease enter another integer:");
    scanf("%d", &c);

    minMax(a, b, c, &min, &max);
    printf("\nMinimum integer is %d\n", min);
    printf("Maximum integer is %d\n", max);

    insertLineSpace();
    printf("===========================================================\n");
    insertLineSpace();

    //======================================================================================
    // Question B
    //======================================================================================
    int f = 0;
    int s = 0;

    puts("Please enter an integer:");
    scanf("%d", &f);

    puts("\nPlease enter another integer:");
    scanf("%d", &s);
    
    printf("\nInts before swapping: %d and %d\n", f, s);
    swapInts(&f, &s);
    printf("Ints after swapping: %d and %d\n", f, s);
    
    return 0;
}
