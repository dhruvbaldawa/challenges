/*
Description:

My father owned a very old HP calculator. It was in reverse polish notation
(RPN). He would hand me his calculator and tell me "Go ahead and use it". Of
course I did not know RPN so everytime I tried I failed. So for this challenge
we will help out young coder_d00d. We will take a normal math equation and
convert it into RPN. Next week we will work on the time machine to be able to
send back the RPN of the math equation to past me so I can use the calculator
correctly.

Input:

A string that represents a math equation to be solved. We will allow the 4
functions, use of () for ordering and thats it. Note white space between
characters could be inconsistent. Number is a number "+" add "-" subtract "/"
divide "x" or "*" for multiply "(" with a matching ")" for ordering our
operations

Output:

The RPN (reverse polish notation) of the math equation.
Challenge inputs:

Note: "" marks the limit of string and not meant to be parsed.
 "0+1"
 "20-18"
 " 3               x                  1   "
 " 100    /                25"
 " 5000         /  ((1+1) / 2) * 1000"
 " 10 * 6 x 10 / 100"
 " (1 + 7 x 7) / 5 - 3  "
 "10000 / ( 9 x 9 + 20 -1)-92"
 "4+5 * (333x3 /      9-110                                      )"
 " 0 x (2000 / 4 * 5 / 1 * (1 x 10))"
*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define STACK_SIZE 256

typedef struct stack_struct {
    int top;
    int elements[STACK_SIZE];
} stack_t;

void stack_init(stack_t* s) {
    s->top = -1;
}

int stack_push(stack_t* s, int el) {
    if (s->top == STACK_SIZE) {
        return 0;
    } else {
        s->elements[++s->top] = el;
        return 1;
    }
}

int stack_pop(stack_t* s) {
    if (s->top == -1) {
        return -1;
    } else {
        return s->elements[s->top--];
    }
}

int stack_empty(stack_t* s) {
    return s->top == -1;
};

void stack_print(stack_t* s) {
    printf("\nStack: \n");
    for(int i=s->top; i >= 0; i--) {
        printf("%d\n", s->elements[i]);
    }
}

int main(int argc, char* argv[]) {
    char* instring = argv[1];
    // to make sure that the result has something useful
    int result_flag = 0;
    // the current result value
    int result = 0;
    // create stack and initialize all its variables
    stack_t s;
    stack_init(&s);

    int i = 0;
    while (1) {
        char inchar = instring[i];
        printf("%c", inchar);

        if (isdigit(instring[i])) {
            result_flag = 1;
            int value = atoi(&inchar);
            result = result * 10 + value;
        } else {
            // put any existing result into the stack
            if (result_flag) {
                stack_push(&s, result);
                result = 0;
                result_flag = 0;
            }

            switch(inchar) {
                case '/':
                case '*':
                case '+':
                case '-':
                    // @TODO: checks for empty stack
                    int a = stack_pop(&s);
                    int b = stack_pop(&s);
                    printf("%d %d %c", a, b, inchar);
                    break;
            }
        }

        if (inchar == '\0') {
            break;
        }

        i++;
    }

    stack_print(&s);
    return 0;
}
