# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


letter_path = r"./Input/Letters/starting_letter.txt"
names_path = r"./Input/Names/invited_names.txt"
output_letters_path = r"./Output/ReadyToSend"

letter_open = open(letter_path, "r")
letter_read = letter_open.read()

names = open(names_path, "r")
names_read = names.readlines()


for n in names_read:
    name = n.strip()
    letter = letter_read.replace("[name]", name)
    f = open(f"{output_letters_path}/letter_for_{name}.txt", "w")
    f.write(letter)
    f.close()


letter_open.close()
names.close()
print("\nAll letters saved.")

