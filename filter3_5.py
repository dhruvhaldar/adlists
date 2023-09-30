import re

def remove_comments(text):
  """Removes comments from a string."""
  pattern = r"# \[(.*?)\]"
  return re.sub(pattern, "", text)

def remove_blank_lines(lines):
  """Removes blank lines from a list of strings."""
  new_lines = []
  for line in lines:
    if line.strip():
      new_lines.append(line)
  return new_lines

# Read the adaway.txt file
with open("adaway.txt", "r") as f:
  lines = f.readlines()

# Remove blank lines
lines = remove_blank_lines(lines)

# Remove the comments
lines = [remove_comments(line) for line in lines]

# Write the modified lines to a new file
with open("new_adaway.txt", "w") as f:
  for line in lines:
    f.write(line)
