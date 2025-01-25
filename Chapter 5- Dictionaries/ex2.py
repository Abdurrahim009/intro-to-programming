glossary = {

    "variable": "A container for storing data values.",
    "list": "A collection of items in a particular order.",
    "loop": "A sequence of instructions that is continually repeated until a certain condition is met.",
    "function": "A block of code that only runs when it is called.",
    "dictionary": "A collection of key-value pairs."

}


for word, meaning in glossary.items():
    
    print(f"{word.capitalize()}:\n{meaning}\n")

