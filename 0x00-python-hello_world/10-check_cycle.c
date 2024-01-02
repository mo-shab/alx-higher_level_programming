#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks cycle in a singly-linked list
 * @list: The list
 *
 * Return: 0 if no cycle.
 * 1 if cycle found.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
