#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - printing info of a python list
 * @p: object
 *
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;
	ssize_t size;

	size = PyList_Size(p);
	PyListObject *lis_ob = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", lis_ob->allocated);

	while (i < size)
	{
		printf("Element %d: %s\n", i, Py_TYPE(lis_ob->ob_item[i])->tp_name);
		i++;
	}
}
