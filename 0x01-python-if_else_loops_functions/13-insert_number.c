#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserting a node in a sorted linked list
 * @head: head of linked list
 * @number: data of new node to insert
 *
 * Return: address for new node inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *walker1, *walker2, *new_n;

	walker1 = *head;
	new_n = malloc(sizeof(listint_t));
	if (new_n == NULL)
		return NULL;
	new_n->n = number;
	new_n->next = NULL;
	if (walker1 == NULL)
	{
		*head = new_n;
		return (new_n);
	}
	if (walker1->n >= number)
	{
		new_n->next = walker1;
		*head = new_n;
		return (new_n);
	}
	walker2 = walker1->next;
	while (walker2 != NULL)
	{
		if (walker2->n >= number)
		{
			new_n->next = walker2;
			walker1->next = new_n;
			return (new_n);
		}
		walker1 = walker2;
		walker2 = walker1->next;
	}
	walker1->next = new_n;
	return (new_n);
}
