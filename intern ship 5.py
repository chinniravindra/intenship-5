def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def save_to_file(reversed_text):
    filename = input("Enter filename to save (e.g., output.txt): ")
    try:
        with open(filename, 'w') as file:
            file.write(reversed_text)
        print(f"Reversed text saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

def main():
    while True:
        print("\n--- Text Reverser ---")
        print("1. Reverse character order")
        print("2. Reverse word order")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice not in ['1', '2', '3']:
            print("Invalid option. Please try again.")
            continue
        
        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        text = input("Enter text to reverse: ").strip()
        if not text:
            print("Input cannot be empty. Please enter valid text.")
            continue
        
        if choice == '1':
            result = reverse_characters(text)
        else:
            result = reverse_words(text)
        
        print("Reversed Text:", result)
        
        save_option = input("Do you want to save the result to a file? (yes/no): ").lower()
        if save_option == 'yes':
            save_to_file(result)

if __name__ == "__main__":
    main()
