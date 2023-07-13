## Code to generate list of stories from directory and allow user to choose which to open
import os

def list_text_files(directory):
    text_files = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            text_files.append(file)
    return text_files

def open_file(directory, filename):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'r') as f:
        story = f.read()
        return story

# Example usage:
directory_path = "stories"

# List text files in the directory
text_files = list_text_files(directory_path)
if not text_files:
    print("\nNo text files found in the directory.")
else:
    print("\nThese are the text files available to play madlibs:")
    for i, file in enumerate(text_files, start=1):
        print(f"{i}. {file}")

    # Prompt the user to choose a file
    choice = input("\nEnter the number of the file you want to open (or 'q' to quit): ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(text_files):
            selected_file = text_files[index]
            story = open_file(directory_path, selected_file)
        else:
            print("Invalid choice.")
    elif choice.lower() == "q":
        print("Quitting...")
    else:
        print("Invalid choice.")


#with open("stories\story2.txt","r") as f:
#    story = f.read()
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1].lower()
        words.add(word)
        start_of_word = -1

answers= {}
#words = sorted(words)
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word.lower(), answers[word])

print(story)