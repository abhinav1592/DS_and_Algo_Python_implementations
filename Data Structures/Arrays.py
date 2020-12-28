'''
Arrays in Python.

Reference: https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/
TYPE CODE	C TYPE	            PYTHON TYPE	MINIMUM SIZE IN BYTES
‘b’	        signed char	            int	                1
‘B’	       	unsigned char	       	int	            	1
‘u’	       	Py_UNICODE	       	unicode character	    2
‘h’	       	signed short	       	int	            	2
‘H’	       	unsigned short	       	int	            	2
‘i’	       	signed int	       	    int	            	2
‘I’	       	unsigned int	       	int	            	2
‘l’	       	signed long	       	    int	            	4
‘L’	       	unsigned long	       	int	            	4
‘q’	       	signed long long	    int	            	8
‘Q’	       	unsigned long long	    int	            	8
‘f’	       	float	       	       float	           	4
‘d’	       	double	       	       float            	8


'''
import array
import time
timestr = time.strftime("%Y%m%d-%H%M%S")


class ArrayMethods:
    def __init__(self, size, type):
        if type == 'integer':
            self.items = array.array('i', [0] * size)
        if type == 'float':
            self.items = array.array('d', [0.0]*size)

    def check_for_empty_array(self):
        if not self.items or len(self.items) == 0:
            print("Array is not initialized yet or it's empty")

    def insert_at_any_index(self, index, item):
        self.items.insert(index, item)

    def delete_from_any_index(self, index):
        if self.check_for_empty_array():
            self.items.pop(index)

    def delete_first_occurence_of_item(self, item):
        self.items.remove(item)

    def traverse(self):
        # Loop through the list and print item only
        print("Loop through the list and printing item only")
        if self.items and len(self.items) != 0:
            for x in self.items:
                print("x: %s" % x)
            print("------------------------------------------------")
            print("Loop through the list and printing index and item")
            for i, x in enumerate(self.items):
                print("i: %s, x: %s" % (i, x))
            print("------------------------------------------------")
            print("Loop through the array using range")
            for i in range(len(self.items)):
                print("i: %s, element: %s" % (i, self.items[i]))

    def slice_between_i_and_j(self, i, j):
        print("slice_between_i_and_j, self.items: %s" % self.items[i:j])

    def extend_by_n(self, n):
        self.items.extend(array.array('i', [0]*n))

    def print_array(self):
        print("self.items: %s" % self.items)

    def reverse_array(self):
        self.items.reverse()

    def write_array_to_file_object_as_bytes(self):
        filename = "Arrays" + timestr + ".txt"
        print("Writing array to file: %s" % filename)
        self.items.tofile(open("Arrays" + timestr +".txt", 'wb'))

    def count_occurences(self, item):
        print("Item: %s appears %s times in Items array" % (item , self.items.count(item)))

    def convert_to_python_list(self):
        print("List: %s" % self.items.tolist())

    def get_current_length(self):
        return len(self.items)

x = ArrayMethods(10, 'integer')
#x.traverse()
x.insert_at_any_index(0, 4)
x.print_array()
# x.insert_at_any_index(1, 4)
# x.print_array()
# x.insert_at_any_index(2, 4)
# x.print_array()
# x.insert_at_any_index(3, 4)
# x.print_array()
# x.insert_at_any_index(4, 4)
# x.print_array()
length_of_Array = x.get_current_length()
x.insert_at_any_index(length_of_Array, 14)
x.print_array()
x.insert_at_any_index(-1, 15) # Try not to use negative indexes
x.print_array()
x.delete_first_occurence_of_item(0)
x.print_array()
x.reverse_array()
x.print_array()
#x.write_array_to_file_object_as_bytes()
#x.print_array()
x.count_occurences(0)
x.convert_to_python_list()
x.slice_between_i_and_j(4, 8)
x.print_array()


y = ArrayMethods(10, 'float')
y.insert_at_any_index(0, 4.5)
y.insert_at_any_index(0, 3.6)
y.print_array()