#include "lists.h"

/**
* print_dlistint - Function that print all element on a list
* @dlistint_t: the list to be printed
* Return: number of nodes
*/

size_t print_dlistint(const dlistint_t *h)
{
	int n = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		n++;
		h = h->next;
	}

	return (n);
}
