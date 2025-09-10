from collections import Counter

def word_count_analysis(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()

        lines = text.splitlines()
        words = text.split()
        characters = len(text)

       
        word_freq = Counter(word.strip(".,!?;:").lower() for word in words)

        print("\nText Analysis Results 📊")
        print(f"Total Lines: {len(lines)}")
        print(f"Total Words: {len(words)}")
        print(f"Total Characters: {characters}")
        print("\nTop 10 Most Common Words:")
        for word, count in word_freq.most_common(10):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f" Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")



file_name = "sample.txt"
word_count_analysis(file_name)
