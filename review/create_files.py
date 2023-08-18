#!/bin/python

print("open text file foe  edit")

my_file = open("w+", "test.txt")
my_file.write("test")
my_file.close()
