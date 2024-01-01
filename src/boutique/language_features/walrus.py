import pathlib
import sys

for filename in sys.argv[1:]:
    path = pathlib.Path(filename)
    counts = [
        (text := path.read_text()).count("\n"),  # Number of lines
        len(text.split()),  # Number of words
        len(text),  # Number of characters
    ]
    print(*counts, path)
    
    
while (command := input("your choice: ")) != "q":
     print("Your input:", command)
     
print(command)

class ContextManager:
    def __enter__(self):
        print("Entering the context...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Leaving the context...")

with ContextManager() as context:
    print(context)  # None

with (context := ContextManager()):
    print(context)  # <__main__.ContextManager object at 0x7fb551cdb9d0>

v = [y for x in s if (y := math.sin(x)) >= 0]
