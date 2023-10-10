#include <stdlib.h>
#include "lists.h"

/**
 * num_ofnodes - function calculating number of nodes
 * @head: head of linked list
 *
 * Return: integeras num of nodes
 */
int num_ofnodes(listint_t **head)
{
	listint_t *walker;
	int num = 0;

	walker = *head;
	while (walker != NULL)
	{
		walker = walker->next;
		num++;
	}
	return (num);
}

/**
 * is_palindrome - checking if the single linked list
 * is palindrome (like a mirror)
 *
 * @head: head of linked list
 *
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *walker1, *walker2;
	int n, i, j;

	n = num_ofnodes(&(*head));
	walker1 = *head;
	if (n < 2)
		return 1;
	for (i = 0; i < (n / 2); i++)
	{
		walker2 = walker1;
		for (j = i; j < n - i - 1; j++)
		{
			walker2 = walker2->next;
		}
		if (walker1->n != walker2->n)
			return 0;
		walker1 = walker1->next;
	}
	return 1;
}
