import re
import pathlib
script_path = pathlib.Path(__file__).parent.resolve()

f = open(script_path + "input.txt", "r")
f = open(script_path + "test_input.txt", "r")
a = f.readline()

row = 1
while a:


    a = f.readline()
    row += 1