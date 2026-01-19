/*
Lab 8 - PROG1955
Matt Cunningham
11/21/2025
*/


#include <stdio.h>

void clrStream(void);
void clrStream(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {
    }
}

struct order {
    char name[20];

    int teaCount;
    int coffeeCount;

    double teaPrice;
    double coffeePrice;

    double teaSubtotal;
    double coffeeSubtotal;

    double itemSubtotal;

    double orderTaxes;

    double orderCostTotal;
};

int placeOrder(struct order *newOrder);
int placeOrder(struct order* newOrder) {
    puts("Welcome to the C Language Coffee Shop!\n");

    int itemNumber = 0;
    int choosing = 1;

    int quantity = 0;

    newOrder->teaCount = 0;
    newOrder->coffeeCount = 0;

    newOrder->teaPrice = 2.50;
    newOrder->coffeePrice = 1.50;

    newOrder->teaSubtotal = 0.00;
    newOrder->coffeeSubtotal = 0.00;

    newOrder->itemSubtotal = 0.00;

    newOrder->orderCostTotal = 0.00;


    while (choosing) {
        puts("\nWhat would you like to order?\n 1. Tea \n 2. Coffee");
        scanf("%d", &itemNumber);

        if (itemNumber == 1) {
            puts("\nHow many teas would you like?");
            scanf("%d", &quantity);
            newOrder->teaCount += quantity;
        }
        else if (itemNumber == 2) {
            puts("\nHow many coffees would you like?");
            scanf("%d", &quantity);
            newOrder->coffeeCount += quantity;
        }

        puts("\nWould you like to order anything else? \n 0. NO \n 1. YES");
        scanf("%d", &choosing);
    }

    puts("\nWhat is the name for the order?");
    clrStream();
    fgets(newOrder->name, sizeof(newOrder->name), stdin);

    newOrder->teaSubtotal = newOrder->teaCount * newOrder->teaPrice;
    newOrder->coffeeSubtotal = newOrder->coffeeCount * newOrder->coffeePrice;

    newOrder->itemSubtotal = newOrder->teaSubtotal + newOrder->coffeeSubtotal;

    newOrder->orderTaxes = 0.13 * newOrder->itemSubtotal;
    newOrder->orderCostTotal = newOrder->itemSubtotal + newOrder->orderTaxes;

}

int main(void)
{
    struct order newOrder;

    placeOrder(&newOrder);

    puts("\nThank you for your order! Here is your receipt: \n");
    puts("C Language Coffee Company Order Receipt\n===========================================");
    printf("Order for: %s\n", newOrder.name);
    puts("Items:");

    if (newOrder.teaCount > 0) {
        printf("\nTEA: ");
        printf("QTY = %d, ", newOrder.teaCount);
        printf("TTL = $%.3lf", newOrder.teaSubtotal);
    }

    if (newOrder.coffeeCount > 0) {
        printf("\nCOFFEE: ");
        printf("QTY = %d, ", newOrder.coffeeCount);
        printf("TTL = $%.3lf", newOrder.coffeeSubtotal);
    }

    printf("\n\nITEM SUBTOTAL: $%.3lf", newOrder.itemSubtotal);
    printf("\nAPPLICABLE TAXES (13%%): $%.3lf", newOrder.orderTaxes);
    printf("\nORDER TOTAL AFTER TAX $%.3lf\n", newOrder.orderCostTotal);
    puts("===========================================");

    return 0;
}
