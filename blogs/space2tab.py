#!/usr/bin/python3

from sys import argv

def space_to_tab(value):
    return value.replace(r"    ", r"\t")


if __name__ == "__main__":
    try:
        filename = argv[1]
    except IndexError:
        print("fatal error: no enough argument")
        print("usage: tab2space.py filename")
        exit(-1)


    try:
        with open(filename, "r") as file:
            result = space_to_tab(file.read())
        with open(filename, "w") as file:
            file.write(result)


    except Exception as error:
        print(f"fatal error: open file '{filename}' failed ({error})")
        exit(-1)

    else:
        print("done. ")

