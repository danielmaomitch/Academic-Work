#ifndef STACK_UTIL_H
#define STACK_UTIL_H

#include "stack.h"
typedef bool (*stack_equals_func)(const void  *elem1, const void *elem2);

void stack_reverse(stack *s);

bool stack_equals(stack *s1, stack *s2, stack_equals_func equals);

#endif /* STACK_UTIL_H */