import re
import pathlib

if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    f = open(script_path + "test_input.txt", "r")
    a = f.readline().strip()

    row = 1
    while a:


        a = f.readline().strip()
        row += 1