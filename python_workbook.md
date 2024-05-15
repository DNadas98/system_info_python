# Setup
```Bash
python3 --version
python3 -m venv myenv
source venv/bin/activate
```

# Basics
```Python
print("Hello, World!")

# Single-line comment
"""
This is a
multi-line comment
"""

x = 10
name = "Asdf"
pi = 3.14


list = [1, 2, 3, 4, 5]

dictionary = {"name": "Asdf", "age": 25} # ~ HashMap

if x > 10:
    print("x is greater than 10")
else:
    print("x is 10 or less")

for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

def greet(name):
    return f"Hello, {name}"

print(greet("Asdf"))

# Simplest I/O

with open("example.txt", "w") as file:
    file.write("Hello, World!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```