#include <stdio.h>
#include <stdlib.h>

typedef struct NODE {
    struct NODE *next;
    int data;
}node;

void addFirst(node *target, int data){

    node *newNode = malloc(sizeof(node));
    newNode -> next = target -> next;
    newNode -> data = data;

    target -> next = newNode;
}

void removeFirst(node *target){

    node *removeNode = target -> next;
    target -> next = removeNode -> next;
    free(removeNode);
}

int main(){

    node *head = malloc(sizeof(node));
    head -> next = NULL;

    addFirst(head, 10);
    addFirst(head, 20);
    addFirst(head, 30);

    removeFirst(head);

    node *curr = head -> next;
    while(curr != NULL){
        printf("%d\n", curr -> data);
        curr = curr -> next;
    }

    curr = head -> next;
    while(curr != NULL){

        node *next = curr -> next;
        free(curr);
        curr = next;
    }

    free(head);
    return 0;
}