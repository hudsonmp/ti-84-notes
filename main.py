import textwrap
from NOTES import notes

# TI-84 CE Python screen width is 26 characters
CALCULATOR_WIDTH = 26

key = input("Search term: ")

if key in notes:
    note_content = notes[key]
    # Wrap the note content for better display on the calculator screen
    for line in textwrap.wrap(note_content, width=CALCULATOR_WIDTH):
        print(line)
else:
    print("No exact match. Suggestions:")
    suggestions = []
    search_term_lower = key.lower()
    # Split search term into words, removing empty strings that might result from multiple spaces
    search_words = [word for word in search_term_lower.split() if word]

    if not search_words: # Handle empty or space-only search input
        print("   Please enter a non-empty search term.")
    else:
        for note_key_original in notes: # Iterate through original keys to display them as is
            note_key_lower = note_key_original.lower()
            
            # Fuzzy and Partial Search Logic:
            # All words in the search term must be present as substrings in the note key.
            all_search_words_found_as_substrings = True
            for s_word in search_words:
                if s_word not in note_key_lower: # Check if each search word is a substring
                    all_search_words_found_as_substrings = False
                    break
            
            if all_search_words_found_as_substrings:
                # Add to suggestions, ensuring no duplicates if this loop somehow re-evaluates
                if note_key_original not in suggestions:
                    suggestions.append(note_key_original)

        if suggestions:
            for s in sorted(suggestions): # Sort suggestions alphabetically for consistent output
                print("  ", s)
        else:
            print("   No similar terms found.")