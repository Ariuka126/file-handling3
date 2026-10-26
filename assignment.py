# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    if line_number <= 0:
        return ""

    file = open(filename, "r")
    line = ""
    for _ in range(line_number):
        line = file.readline()
        if line == "":
            break
    file.close()

    if line != "":
        if line.endswith("\n"):
            line = line[:-1]
        return line
    return ""
# Exercise 2
def reverse_lines(source, destination):
    # Write your code here
    pass

# Exercise 3
def merge_files(first, second, destination):
    # Write your code here
    pass

# Exercise 4
def find_score(filename, name):
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
