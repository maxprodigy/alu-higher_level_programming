#include "lists.h"
#include <stdio.h>

/**
 *is_palindrome - Checks if a singly linked list is a palindrome
 *
 *@head: Head of singly linked list
 *Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	return (is_palindromeUtil(*head, head));
}

/**
 *is_palindromeUtil - Used to find if a singly linked list is a palindrome
 *@left: The left side of the list
 *@right: The right side of the list
 *Return: 1 if list is a palindrome, 0 if not
 */
int is_palindromeUtil(listint_t *right, listint_t **left)
{
	int is_p, is_p1;

	if (right == NULL)
		return (1);

	is_p = is_palindromeUtil(right->next, left);
	if (is_p == 0)
		return (0);
	is_p1 = (right->n == (*left)->n);
	(*left) = (*left)->next;
	return (is_p1);
}
