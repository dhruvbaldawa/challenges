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
#define BUFFER_SIZE 256
#define TRUE 1
#define FALSE 0
char const* OPERATORS = "(*/+-)";

enum op_enum {
    OPEN_BRACKET,
    MULTIPLY,
    DIVIDE,
    ADD,
    SUBTRACT,
    CLOSE_BRACKET,
};

typedef struct stack_struct {
    int top;
    int elements[STACK_SIZE];
} stack_t;

void stack_init(stack_t* s) {
    s->top = -1;
}

int stack_push(stack_t* s, int el) {
    if (s->top == STACK_SIZE) {
        return FALSE;
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

int stack_peek(stack_t* s) {
    // @TODO: empty constraint checking
    return s->elements[s->top];
}

int stack_isempty(stack_t* s) {
    return s->top == -1;
};

void stack_print(stack_t* s) {
    printf("\nStack: \n");
    for(int i=s->top; i >= 0; i--) {
        printf("%d\n", s->elements[i]);
    }
}

int can_be_printed(int op) {
    return (op != OPEN_BRACKET && op != CLOSE_BRACKET);
}

int main(int argc, char* argv[]) {
    char* instring = argv[1];
    char output_buffer[BUFFER_SIZE] = "";
    // to make sure that the result has something useful
    int result_flag = FALSE;
    // the current result value
    int result = 0;
    // create stack and initialize all its variables
    stack_t num_stack, op_stack;
    stack_init(&num_stack);
    stack_init(&op_stack);

    int i = 0;
    while (1) {
        char inchar = instring[i];

        if (isdigit(instring[i])) {
            result_flag = TRUE;
            int value = atoi(&inchar);
            result = result * 10 + value;
        } else {
            // put any existing result into the stack
            if (result_flag) {
                sprintf(output_buffer, "%s %d", output_buffer, result);
                result_flag = FALSE;
                result = 0;
            }
            int op = -1;
            switch(inchar) {
                case '/':
                    op = DIVIDE;
                    break;
                case '*':
                    op = MULTIPLY;
                    break;
                case '+':
                    op = ADD;
                    break;
                case '-':
                    op = SUBTRACT;
                    break;
                case '(':
                    op = OPEN_BRACKET;
                    break;
                case ')':
                    op = CLOSE_BRACKET;
                    break;
            }

            // if the character was an operator
            if (op != -1) {
                if (stack_isempty(&op_stack)) {
                    stack_push(&op_stack, op);
                } else {
                    int current_top = stack_peek(&op_stack);
                    // if current top is of higher precedence
                    if (op > current_top) {
                        int stack_top = stack_pop(&op_stack);
                        if (can_be_printed(stack_top)) {
                            sprintf(output_buffer, "%s %c", output_buffer,
                                    OPERATORS[stack_top]);
                        }
                    }
                    stack_push(&op_stack, op);
                }
            }
        }

        if (inchar == '\0') {
            break;
        }

        i++;
    }

    while (!stack_isempty(&op_stack)) {
        int stack_top = stack_pop(&op_stack);
        if (can_be_printed(stack_top)) {
            sprintf(output_buffer, "%s %c", output_buffer, OPERATORS[stack_top]);
        }
    }

    printf("%s\n", output_buffer);
    return 0;
}
