def find_and_replace(file_name, old_word, new_word):
    try:
      
        with open(file_name, "r") as file:
            content = file.read()

       
        if old_word in content:
            updated_content = content.replace(old_word, new_word)
            print(f"Replaced all occurrences of '{old_word}' with '{new_word}'.")
        else:
            updated_content = content
            print(f"'{old_word}' not found in the file.")

       
        with open(file_name, "w") as file:
            file.write(updated_content)
            print("File updated successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except PermissionError:
        print(f" Error: You don’t have permission to modify '{file_name}'.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

file_name = "sample.txt"
old_word = input("Enter the word to find: ")
new_word = input("Enter the replacement word: ")

find_and_replace(file_name, old_word, new_word)
