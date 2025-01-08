#include<stdio.h>
#include<stdlib.h>
#define MAX_SIZE 10
/* This program is implementation stack operation using  array
*/
typedef struct {
    int items[MAX_SIZE];
    int top;
} stack_t;

void init_stack(stack_t *stack){
    stack->top = -1;
}

int is_empty(stack_t *stack){
    return (stack->top == -1);
}

void push(stack_t *stack, int n){
    // push the element with key n 
    if (stack->top == MAX_SIZE-1){
        fprintf(stderr, "Stack overflow\n");
        exit(1);
    }
    stack->items[++(stack->top)] = n;
}

int pop(stack_t *stack){
    if (is_empty(stack)){
        fprintf(stderr, "Stack underflow\n");
        exit(1);
    }
    return stack->items[(stack->top)--];
}

void print_stack(stack_t *stack){
    for(int i =0; i<MAX_SIZE; i++){
        printf("    +------+\n");
        printf(" %-2d | ", i+1);
        if (i>stack->top){
            printf("     |");
        }
        else {
            printf("%d   |", (stack->items[i]));
        }
        printf("\n");
    }
    printf("    +------+\n");
}

int main(){
    stack_t *s;
    init_stack(s);
    push(s, 10);
    push(s, 20);
    push(s, 30);
    push(s, 40);
    print_stack(s);
    int key =  pop(s);
    printf("value popped : %d\n", key);
    printf("\n");
    print_stack(s);
}