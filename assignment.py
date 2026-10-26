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
    src_file = open(source, "r")
    lines = src_file.readlines()
    src_file.close()

    dest_file = open(destination, "w")
    count = 0
    # Process lines in reverse order
    for line in reversed(lines):
        cleaned_line = line.strip()
        dest_file.write(cleaned_line + "\n")
        count += 1

    dest_file.close()
    return count


# Exercise 3
def merge_files(first, second, destination):
    file1 = open(first, "r")
    lines1 = file1.readlines()
    file1.close()

    file2 = open(second, "r")
    lines2 = file2.readlines()
    file2.close()

    dest_file = open(destination, "w")
    count = 0

    for line in lines1:
        dest_file.write(line)
        count += 1

    for line in lines2:
        dest_file.write(line)
        count += 1

    dest_file.close()
    return count
# Exercise 4
def find_score(filename, name):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        if parts[0] == name:
            return int(parts[1])

    return -1

# Exercise 5
def update_score(filename, name, new_score):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    found = False
    updated_lines = []

    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            updated_lines.append(line)
            continue

        parts = cleaned_line.split(",")
        if parts[0] == name:
            updated_lines.append(f"{name},{new_score}\n")
            found = True
        else:
            # Ensure line preserves original ending format or gets proper newline
            if not line.endswith("\n"):
                updated_lines.append(line + "\n")
            else:
                updated_lines.append(line)

    if found:
        file = open(filename, "w")
        for line in updated_lines:
            file.write(line)
        file.close()

    return found
