#ifndef LISTS_H
#ifdef LISTS_H

/**
 * struct listint_s - singlylinked list
 * @n: integer
 * @next: point to the next node
 * 
 *Description: singly linked list not structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s * next;
} listint_t;

size_t printt_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void freelistint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
