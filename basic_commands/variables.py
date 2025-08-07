# examples of variables in Python
# Integer variable
integer_var = 10    
# Float variable
float_var = 20.5
# String variable
string_var = "Hello, World!"
# Boolean variable
boolean_var = True
# List variable
list_var = [1, 2, 3, 4, 5]
# Tuple variable
tuple_var = (1, 2, 3)
# Dictionary variable
dict_var = {"name": "Alice", "age": 30}
# Set variable
set_var = {1, 2, 3, 4, 5}
# None variable
none_var = None
# Complex number variable
complex_var = 2 + 3j
# Bytes variable
bytes_var = b"Hello, Bytes!"
# Frozen set variable
frozenset_var = frozenset([1, 2, 3, 4, 5])
# Bytearray variable
bytearray_var = bytearray(b"Hello, Bytearray!")
# Range variable
range_var = range(10)  # Represents numbers from 0 to 9
# Memory view variable
memoryview_var = memoryview(bytes_var)  # Memory view of bytes_var
# Example of a variable with a function
def example_function():
    return "This is an example function."
# Function variable
function_var = example_function
# Class variable
class ExampleClass:
    def __init__(self, value):
        self.value = value
# Instance of class variable
example_class_instance = ExampleClass(42)
# Module variable
import math
module_var = math  # Refers to the math module
# File variable
file_var = open("example.txt", "w")  # File object variable
# Close the file variable
file_var.close()  # Always close the file after use
# Generator variable
def example_generator():
    for i in range(5):
        yield i * 2  # Yields even numbers from 0 to 8
generator_var = example_generator()  # Generator object variable
# Iterator variable
iterator_var = iter(list_var)  # Creates an iterator from list_var
# Context manager variable
from contextlib import contextmanager
@contextmanager
def example_context_manager():
    print("Entering context")
    yield
    print("Exiting context")
# Using the context manager
with example_context_manager() as cm:
    print("Inside context manager")
# Regular expression variable
import re
regex_var = re.compile(r"\d+")  # Compiled regular expression to match digits
# File path variable
file_path_var = "path/to/file.txt"  # String representing a file path
# JSON variable
import json
json_var = json.dumps({"name": "Bob", "age": 25})  # JSON string representation
# XML variable
import xml.etree.ElementTree as ET
xml_var = ET.Element("root")  # XML element variable

# XML element with text
xml_var.text = "This is an XML element."
# XML element with attributes
xml_var.set("attribute", "value")  # Setting an attribute for the XML element
# XML tree variable
xml_tree_var = ET.ElementTree(xml_var)
# XML tree variable with a root element
xml_tree_var = ET.ElementTree(ET.Element("root"))  # XML tree with a root element
# XML tree variable with a child element
child_element = ET.SubElement(xml_tree_var.getroot(), "child")
child_element.text = "This is a child element."  # Adding text to the child element

# XML tree variable with multiple child elements
for i in range(3):
    child = ET.SubElement(xml_tree_var.getroot(), "child")
    child.text = f"This is child element {i + 1}."
# XML tree variable with attributes in child elements
for i in range(3):
    child = ET.SubElement(xml_tree_var.getroot(), "child")
    child.text = f"This is child element {i + 1}."
    child.set("id", str(i + 1)) # Setting an attribute for each child element

# XML tree variable with nested elements