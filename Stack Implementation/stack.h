#ifndef stack_H
#define stack_H

#include <stdbool.h>

/**
 * Name of the node struct used by stack.
 */
typedef struct node node;

/**
 * The node struct definition.
 */
struct node {
    void *elem;
    node *next;
};

/**
 * Name of the stack struct.
 */
typedef struct stack stack;

/**
 * The stack struct definition.
 */
struct stack {
    node *top;
    size_t size;
};

/**
 * Pointer to function that prints an element.
 */
typedef void (*print_elem_func)(const void *elem);

/* 
 * Pointer to function that frees an element.
 */
typedef void (*free_elem_func)(void *elem);

stack *stack_init();

bool stack_is_empty(const stack *s);

size_t stack_size(const stack *s);

bool stack_push(stack *s, void *elem);

void *stack_pop(stack *s);

/**
 * Free the memory associated with a stack. If
 * free_elem is not NULL, then the memory for each element
 * is also freed by calling the provided function;
 * otherwise, the elements are not freed.
 */
void stack_free(stack *s, free_elem_func free_elem);

/**
 * Prints the elements of the stack where each element is
 * printed using the provided function. Undefined behavior
 * results if print_elem is NULL.
 */
void stack_print(const stack *s, print_elem_func print_elem);

#endif // stack_H