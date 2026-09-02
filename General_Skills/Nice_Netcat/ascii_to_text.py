import sys

# Ensure a file argument was provided to prevent an IndexError
if len(sys.argv) < 2:
    print("Error: Please provide an input file path.")
    print("Usage: python script.py <filename>")
    sys.exit(1)

file = sys.argv[1]

# 1. FIX: Initialize flag as an empty string instead of None
flag = ""

with open(file, 'r', encoding='utf-8') as files:
    for lines in files:
        clean_line = lines.rstrip("\n")        
        # Skip empty lines to prevent int() conversion errors
        if not clean_line:
            continue
        # 2. Convert ASCII number to character and append it to the string
        flag = flag + chr(int(clean_line))
print("Flag :", flag)

