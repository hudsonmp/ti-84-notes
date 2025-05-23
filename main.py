import textwrap
from pprint import pprint

# TI-84 CE Python screen width is 26 characters
CALCULATOR_WIDTH = 26

def format_note(title, content):
    wrapped_content = textwrap.fill(content, width=CALCULATOR_WIDTH)
    
    return {
        'title': title,
        'content': wrapped_content
    }

def create_notes():
    notes = []
    
    math_note = format_note(
      """
      Write here!
      """
    )
    notes.append(math_note)
    
    return notes

def export_notes(notes, filename="calculator_notes.py"):
    with open(filename, 'w') as f:
        f.write("notes = ")
        pprint(notes, stream=f, width=CALCULATOR_WIDTH)

if __name__ == "__main__":
    # Create your notes
    my_notes = create_notes()
    
    # Print preview of notes
    print("Preview of formatted notes:")
    pprint(my_notes, width=CALCULATOR_WIDTH)
    
    # Export notes to a file
    export_notes(my_notes)
    print("\nNotes exported to calculator_notes.py")
