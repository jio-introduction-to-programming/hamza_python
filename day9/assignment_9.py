"""
Part A: Differences between Modules and Packages in python.

Packages and modules are essential components that aid in code organization and reusability. A module is a single file containing Python code, while a package is a collection of modules organized in a directory hierarchy.
Modules enable code reuse by grouping related functionality together. For instance, the "math" module provides various mathematical functions, and the "datetime" module deals with date and time operations.

Modules can be created using simple scripts, on the other hand packages, contain multiple modules in directories and subdirectories.

Packages, on the other hand, allow for higher-level organization by containing multiple related modules. The package hierarchy follows directories and subdirectories. For instance, the "numpy" package deals with numerical computations, containing sub-modules like "numpy.random" for random number generation.

In summary, modules are individual Python files containing code, while packages are directories with multiple modules. Both contribute to Python's modularity and facilitate code management and reuse.

In summary, modules are individual Python files containing code, while packages are directories with multiple modules. Both contribute to Python's modularity and facilitate code management and reuse.

Module:
import math
print(math.sqrt(25))

import datetime
print(datetime.datetime.now())

Package:
import requests
r = requests.get(‘url’)
r.status_code

import numpy as np
a = np.array([[1+2j, 2+1j], [3, 4]])
b = np.array([[5, 6+6j], [7, 8+4j]])
print(a+b)
"""

#Part B: Module math_operations.py

#Main File:
import math_operations

x = 10
y = 5

# Usage of math_operations functions
print("Addition:", math_operations.add(x, y))
print("Subtraction:", math_operations.subtract(x, y))
print("Multiplication:", math_operations.multiply(x, y))

try:
    print("Division:", math_operations.divide(x, y))
except ValueError as e:
    print(e)


"""
Output:
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
"""


"""
Part C: Commomnly used Package

"Pandas" is a commonly used third-party package on PyPI. Pandas offers Python users high-performance, user-friendly data structures and tools for data analysis. It is a strong library for data wrangling and analysis because its main use is to handle and alter structured data.

The primary capabilities of Pandas include:

DataFrame: A two-dimensional tabular data structure, akin to a spreadsheet or a SQL table, that enables effective data manipulation.

Pandas has routines for handling duplicate values and missing data.

Data selection and filtering: It makes it simple to slice, filter, and query data.

Data grouping and aggregation are made possible using Pandas.

Combining data from many sources based on shared columns is known as merging and joining.

Support for processing time-based data and date functionalities is provided for time series analysis.


To install numpy: pip install pandas
Use:
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

In this example, we import Pandas as "pd," create a DataFrame using the dictionary "data," and display the DataFrame. Pandas is a versatile package, widely used in data science, data engineering, and other analytical applications.
"""