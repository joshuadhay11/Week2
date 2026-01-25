'''
Copyright (c) 2016 Python Forensics, Inc. 
                   
Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

'''

#
# Exp Numeric and Bitwise Operations
# Python Fundementals
# Python Forensics, Inc.
# Python Version 3.x
# December 2019
# Version 2.0

#
#Python Numeric Operations
#

print("\nPython Numeric Operations\n")

x = 7
y = 4
print("x:    ",x)
print("y:    ",y)
print("x+y:  ",x+y)
print("x*y:  ",x*y)
print("x/y:  ",x/y)
print("x//y: ",x//y)
print("x%y:  ",x%y)
print("-x:   ",-x)
print("+x:   ",+x)
print("x**y: ",x**y)

#
# Python Bitwise Operations
#

print("\nPython Boolean Operations\n")

a = 0b1010111
b = 0b0101101
print(a)
print(b)
print(hex(a))
print(hex(b))

print('a      {:08b}'.format(a))
print('b      {:08b}'.format(b))
print('a | b  {:08b}'.format(a | b))
print('a & b  {:08b}'.format(a & b))
print('a ^ b  {:08b}'.format(a ^ b))
print('a << 2 {:010b}'.format(a << 2))
print('a >> 2 {:08b}'.format(a >> 2))

# 
# Binary and Hex Rendering 
# Using the format method
#

print("\nPython Boolean Binary and Hex Rendering\n")

value = 254

print('Dec', value)
print('Hex {:02X}'.format(value))
print('Bin {:08b}'.format(value))


