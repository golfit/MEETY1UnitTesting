# Function to print a horizontal border in text
def border(length):
    print(length*"-")
    print(length*"~")
    print(length*"-")

# Function to print text surrounded by a border
def print_with_border(text, length):
    border(length)
    print(text)
    border(length)

def print_auto_border(text) :
    border(len(text))
    print(text)
    border(len(text))

# Test Program
print_with_border("This is my program!", 25)
print_with_border("This is the end of my program.", 10)
