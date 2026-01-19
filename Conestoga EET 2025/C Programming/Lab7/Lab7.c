/*
Lab 7 - PROG1955
Matt Cunningham
11/14/2025
*/

#include <stdio.h>

void clrStream(void);
void clrStream(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {
    }
}

char arrayValue(const char* array, int offset, int length);
char arrayValue(const char* array, int offset, int length) {
    return *(array + offset);
}

void printString(char* array);
void printString(char* array) {
    while (*array != '\0') {
        printf("%c\n", *array);
        array++;
    }
}

int main(void)
{

    //======================================================================================
    // Question A
    //======================================================================================
    int inputting = 1;
    int offset;
    char fiveElArray[5] = { 'A', 'B', 'C', 'D', 'E'};

    while (inputting) {
        puts("Please enter an integer, or type '-1' to end:");
        scanf("%d", &offset);
        clrStream();

        if (offset == -1) {
            inputting = 0;
            puts("See you later!\n");
        }
        else {
            char getCharAtIndex = arrayValue(fiveElArray, offset, 5);
            printf("%c\n\n", getCharAtIndex);
        }
    }

    puts("=================================================================\n");

    //======================================================================================
    // Question B
    //======================================================================================

    char name[50];

    puts("Please enter your name:");
    fgets(name, sizeof(name), stdin);
    printString(name);

    return 0;
}
