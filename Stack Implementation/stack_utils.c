#include <stdio.h>
#include <stdlib.h>
#include "stack_utils.h"

void stack_reverse(stack *s) {
    node *n;
    node *next;
    int steps = s->size - 1;
    void *temp;

    while (steps > 0) {
        n = s->top;
        next = s->top->next;
        for (int i = 0; i < steps; i++) {
            temp = n->elem;
            n->elem = next->elem;
            next->elem = temp;
            n = next;
            next = next->next;
        }
        steps--;
    }
}

bool stack_equals(stack *s1, stack *s2, stack_equals_func equals) {
    node *n1 = s1->top;
    node *n2 = s2->top;
    
    if (s1->size == s2->size) {
        while(n1) {
            if(!(equals(n1->elem, n2->elem))) {
                return false;
            }
            n1 = n1->next;
            n2 = n2->next;
        }
    }

    else {
        return false;
    }

    return true;
}
    