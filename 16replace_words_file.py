def replace_words_in_file(input_file, output_file, replacements):
    with open(input_file, 'r') as infile:
        content = infile.read()

    # Replace words using the dictionary
    for old_word, new_word in replacements.items():
        content = content.replace(old_word, new_word)

    with open(output_file, 'w') as outfile:
        outfile.write(content)

# Example usage
replacements = {"hello": "hi"}  # Define your mapping here

# Input/output file names
input_file = "input.txt"
output_file = "output.txt"

replace_words_in_file(input_file, output_file, replacements)
print(f"Replacements done. Output written to {output_file}")
