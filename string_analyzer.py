from string_package import (reverse_string, capitalize_words,
                            remove_punctuation, count_characters,
                            count_words, average_word_length)

def main():
    # Read sentence from the user
    user_input = input("Please enter a sentence: ")

    # Manipulate the string
    reversed_string = reverse_string(user_input)
    capitalized_string = capitalize_words(user_input)
    cleaned_string = remove_punctuation(user_input)

    # Get statistics
    character_count = count_characters(cleaned_string)
    word_count = count_words(cleaned_string)
    avg_word_length = average_word_length(cleaned_string)

    # print the results
    print(f"Reversed String: {reversed_string}")
    print(f"Capitalized String: {capitalized_string}")
    print(f"Character Count (without punctuation): {character_count}")
    print(f"Word Count (without punctuation): {word_count}")
    print(f"Average Word Length: {avg_word_length:.2f}")

if __name__ == "__main__":
    main()
