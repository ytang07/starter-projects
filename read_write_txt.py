def write_text(filename):
    text = input("What would you write to a text file? ")
    with open(filename, "w") as f:
        f.write(text)

def read_text(filename):
    with open(filename, "r") as f:
        text = f.read()
    return text

write_text("test.txt")
print(read_text("test.txt"))