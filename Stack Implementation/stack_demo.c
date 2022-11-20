#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack_utils.h"

void elem_to_string(const void *s) {
    printf("%s", (char *) s);
}
//*((double *) s1) == *((double *) s2)
bool elem_equals(const void *s1, const void *s2) {
    return strcmp((char *) s1, (char *) s2) == 0;
}

bool two_empty(void) {
    stack *s = stack_init();
    stack *s2 = stack_init();
    stack_print(s, &elem_to_string);
    stack_print(s2, &elem_to_string);
    bool x = stack_equals(s, s2, &elem_equals);
    stack_free(s, NULL);
    stack_free(s2, NULL);
    return x;
}

bool two_equal1(void) {
    stack *s = stack_init();
    stack *s2 = stack_init();
    stack_push(s, "a");
    stack_push(s2, "a");
    stack_print(s, &elem_to_string);
    stack_print(s2, &elem_to_string);
    bool x = stack_equals(s, s2, &elem_equals);
    stack_free(s, NULL);
    stack_free(s2, NULL);
    return x;
}
bool two_unequal1(void) {
    stack *s = stack_init();
    stack *s2 = stack_init();
    stack_push(s, "a");
    stack_push(s2, "b");
    stack_print(s, &elem_to_string);
    stack_print(s2, &elem_to_string);
    bool x = stack_equals(s, s2, &elem_equals);
    stack_free(s, NULL);
    stack_free(s2, NULL);
    return x;
}
bool two_equal3(void) {
    stack *s = stack_init();
    stack *s2 = stack_init();
    stack_push(s, "a");
    stack_push(s, "b");
    stack_push(s, "c");
    stack_push(s2, "a");
    stack_push(s2, "b");
    stack_push(s2, "c");
    stack_print(s, &elem_to_string);
    stack_print(s, &elem_to_string);
    bool x = stack_equals(s, s2, &elem_equals);
    stack_free(s, NULL);
    stack_free(s2, NULL);
    return x;
}
bool two_unequal3(void) {
    stack *s = stack_init();
    stack *s2 = stack_init();
    stack_push(s, "a");
    stack_push(s, "b");
    stack_push(s, "c");
    stack_push(s2, "a");
    stack_push(s2, "b");
    stack_push(s2, "d");
    stack_print(s, &elem_to_string);
    stack_print(s2, &elem_to_string);
    bool x = stack_equals(s, s2, &elem_equals);
    stack_free(s, NULL);
    stack_free(s2, NULL);
    return x;
}

int main(void) {
    stack *s = stack_init();

    // stack_reverse demo
    printf("Original stack: ");
    stack_print(s, &elem_to_string);
    stack_reverse(s);
    printf("Empty stack reverse: ");
    stack_print(s, &elem_to_string);

    stack_push(s, "a");
    printf("Original stack: ");
    stack_print(s, &elem_to_string);
    stack_reverse(s);
    printf("Stack of size 1 reversed: ");
    stack_print(s, &elem_to_string);

    stack_push(s, "b");
    stack_push(s, "c");
    printf("Original stack: ");
    stack_print(s, &elem_to_string);
    stack_reverse(s);
    printf("Stack of size 3 reversed: ");
    stack_print(s, &elem_to_string);

    // stack_equals demo
    printf("Two empty stacks: \n");
    bool result = two_empty();
    printf(result ? "Result: Equal\n" : "Result: Unequal\n");

    printf("Two equal stacks of size 1: \n");
    result = two_equal1();
    printf(result ? "Result: Equal\n" : "Result: Unequal\n");

    printf("Two unequal stacks of size 1: \n");
    result = two_unequal1();
    printf(result ? "Result: Equal\n" : "Result: Unequal\n");

    printf("Two equal stacks of size 3: \n");
    result = two_equal3();
    printf(result ? "Result: Equal\n" : "Result: Unequal\n");

    printf("Two unequal stacks of size 3: \n");
    result = two_unequal3();
    printf(result ? "Result: Equal\n" : "Result: Unequal\n");

    stack_free(s, NULL);
    return 0;
}

