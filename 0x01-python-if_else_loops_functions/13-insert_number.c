#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *runner;
        listint_t *latest;

        runner = *head;

        latest = malloc(sizeof(listint_t));
        if (latest == NULL)
                return (NULL);
        latest->n = number;


        if (*head == NULL || (*head)->n > number)
        {
                latest->next = *head;
                *head = latest;
                return (latest);
        }

        while (runner->next != NULL)
        {
                if ((runner->next)->n >= number)
                {
                        latest->next = runner->next;
                        runner->next = latest;
                        return (latest);
                }

                runner = runner->next;
        }

        new->next = NULL;
        runner->next = latest;
        return (latest);
}
