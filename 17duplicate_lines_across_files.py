from collections import defaultdict

def find_duplicate_lines(filenames):
    line_map = defaultdict(set)

    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f:
                clean_line = line.strip()
                if clean_line:
                    line_map[clean_line].add(filename)

    # Print lines that appear in more than one file
    print("Duplicate lines across files:")
    for line, files in line_map.items():
        if len(files) > 1:
            print(f'"{line}" appears in: {", ".join(files)}')

# Example usage
file_list = ["file1.txt", "file2.txt"]
find_duplicate_lines(file_list)
