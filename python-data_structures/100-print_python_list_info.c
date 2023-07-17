#include <Python.h>

/**
 *print_python_list_info - Prints basic info about python lists
 *@p: A PyObject
 *Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %li: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
