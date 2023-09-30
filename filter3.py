def read_file(filename):
  """Reads a file and returns its contents as a list of strings."""
  with open(filename, "r") as f:
    lines = f.readlines()
  return lines

def remove_blank_lines(lines):
  """Removes blank lines from a list of strings."""
  new_lines = []
  for line in lines:
    if line.strip():
      new_lines.append(line)
  return new_lines

def remove_127_0_0_1(lines):
  """Removes the '127.0.0.1 ' from a list of strings."""
  new_lines = []
  for line in lines:
    if line.startswith("127.0.0.1 "):
      new_line = line[10:]
    else:
      new_line = line
    new_lines.append(new_line)
  return new_lines

def write_file(filename, lines):
  """Writes a list of strings to a file."""
  with open(filename, "w") as f:
    for line in lines:
      f.write(line)

# Read the adaway.txt file
lines = read_file("adaway.txt")

# Remove blank lines
lines = remove_blank_lines(lines)

# Remove the '127.0.0.1 '
lines = remove_127_0_0_1(lines)

# Write the modified lines to a new file
write_file("adaway.txt", lines)