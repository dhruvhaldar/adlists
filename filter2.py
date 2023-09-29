import re

def remove_0000(text_file):
  """Removes 0.0.0.0 from the given text file.

  Args:
    text_file: The path to the text file.
  """

  with open(text_file, "r") as f:
    lines = f.readlines()

  # Compile a regular expression to match 0.0.0.0.
  regex = re.compile(r"0.0.0.0")

  # Remove all occurrences of 0.0.0.0 from the lines.
  for i in range(len(lines)):
    lines[i] = regex.sub("", lines[i])

  # Overwrite the original text file with the modified lines.
  with open(text_file, "w") as f:
    f.writelines(lines)


if __name__ == "__main__":
  # The path to the text file.
  text_file = "spy.txt"

  # Remove 0.0.0.0 from the text file.
  remove_0000(text_file)

  print("0.0.0.0 has been removed from the text file.")
