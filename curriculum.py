"""
curriculum.py
Mobile-friendly Python curriculum content.
"""

CURRICULUM = {
    "Section 1: Setting Up Environment": {
        "Python - Introduction": {
            "theory": (
                "### What is Python?\n\n"
                "Python is a high-level, interpreted, general-purpose programming language conceived by "
                "**Guido van Rossum** in 1989 and officially released in 1991.\n\n"
                "#### Core Design Philosophy (The Zen of Python)\n"
                "- **Readability counts:** Python eliminates bracket boilerplate (`{}`) in favor of clean indentation.\n"
                "- **Explicit is better than implicit:** Code states clearly what it does.\n"
                "- **Simple is better than complex:** Clear, concise code over complicated syntax.\n\n"
                "#### Common Use Cases\n"
                "- **Backend Web Development:** FastAPI, Django, Flask\n"
                "- **Data Science & ML:** Pandas, NumPy, PyTorch\n"
                "- **Automation & Scripting:** Scraping, DevOps, bot workflows\n"
            ),
            "demo_code": (
                "import sys\n\n"
                "print('Hello from Python!')\n"
                "print('Interpreter Version:', sys.version.split()[0])\n"
            ),
            "challenge": "Print a message explaining your primary goal with Python.",
            "solution": "print('I want to build web applications with Python.')",
        },
        "Python Installation (Mac, Linux, Windows)": {
            "theory": (
                "### Installing Python 3\n\n"
                "#### 1. Windows\n"
                "1. Go to python.org/downloads.\n"
                "2. Launch the installer.\n"
                "3. IMPORTANT: Check 'Add python.exe to PATH' before clicking Install.\n\n"
                "#### 2. macOS\n"
                "Run `brew install python` via Homebrew, or use the official package installer from python.org.\n\n"
                "#### 3. Linux (Ubuntu/Debian)\n"
                "Run:\n"
                "`sudo apt update && sudo apt install python3 python3-pip python3-venv -y`\n"
            ),
            "demo_code": (
                "import platform\n"
                "import sys\n\n"
                "print('OS Platform:', platform.system())\n"
                "print('Python Path:', sys.executable)\n"
            ),
            "challenge": "Print your OS platform using `platform.system()`.",
            "solution": "import platform\nprint(platform.system())",
        },
        "PyCharm Installation (Mac, Linux, Windows)": {
            "theory": (
                "### PyCharm IDE Setup\n\n"
                "PyCharm is a dedicated Python IDE built by JetBrains.\n\n"
                "#### Installation Steps\n"
                "1. Download PyCharm Community Edition (free) from jetbrains.com/pycharm/download.\n"
                "2. Run the installer for your OS.\n"
                "3. Enable file association for `.py` files during setup.\n"
            ),
            "demo_code": (
                "import site\n\n"
                "print('Installed package search paths:')\n"
                "for p in site.getsitepackages():\n"
                "    print(f' - {p}')\n"
            ),
            "challenge": "Print a confirmation string that PyCharm Community Edition is installed.",
            "solution": "print('PyCharm Community Edition is ready.')",
        },
        "Checking Python Installation": {
            "theory": (
                "### Verifying Setup in Terminal\n\n"
                "Run these terminal commands:\n"
                "- `python --version` (or `python3 --version`)\n"
                "- `pip --version` (or `python3 -m pip --version`)\n"
            ),
            "demo_code": (
                "import sys\n\n"
                "major = sys.version_info.major\n"
                "minor = sys.version_info.minor\n"
                "print(f'Version detected: {major}.{minor}')\n"
                "print('Ready to code:', major >= 3)\n"
            ),
            "challenge": "Check if `sys.version_info.major == 3` and print 'Passed'.",
            "solution": "import sys\nif sys.version_info.major == 3:\n    print('Passed')",
        },
        "Setting PyCharm: White Theme, Layout & Fonts": {
            "theory": (
                "### PyCharm Customization\n\n"
                "1. **White Theme:** Settings -> Appearance & Behavior -> Appearance -> Theme -> Light.\n"
                "2. **Widescreen Layout:** Right-click an editor tab -> Split Right to see side-by-side files.\n"
                "3. **Fonts:**\n"
                "   - Editor: Settings -> Editor -> Font -> Size 15.\n"
                "   - Terminal: Settings -> Tools -> Terminal -> Font Size 14.\n"
            ),
            "demo_code": (
                "theme = 'Light'\n"
                "editor_font = 15\n"
                "terminal_font = 14\n\n"
                "print(f'Theme: {theme} | Editor Font: {editor_font}pt | Terminal: {terminal_font}pt')\n"
            ),
            "challenge": "Store your preferred font size in a variable `font_size = 15` and print it.",
            "solution": "font_size = 15\nprint(f'Font size: {font_size}')",
        },
    },
    "Section 2: Fundamentals": {
        "print() function": {
            "theory": (
                "### The `print()` Function\n\n"
                "Sends text and values to output.\n\n"
                "- `sep`: separator between elements (default is space).\n"
                "- `end`: string attached at end (default is newline `\\n`).\n"
            ),
            "demo_code": (
                "print('Hello', 'World')\n"
                "print('2026', '09', '27', sep='-')\n"
                "print('Loading', end='... ')\n"
                "print('Complete!')\n"
            ),
            "challenge": "Print numbers 1, 2, 3 separated by ' -> ' and ending with ' [DONE]'.",
            "solution": "print(1, 2, 3, sep=' -> ', end=' [DONE]\\n')",
        },
        "variables": {
            "theory": (
                "### Variables\n\n"
                "Variables refer to memory values. Python determines types dynamically.\n\n"
                "- Must start with letter or underscore `_`.\n"
                "- Cannot start with numbers.\n"
                "- Case-sensitive.\n"
            ),
            "demo_code": (
                "username = 'Coder'\n"
                "level = 5\n"
                "xp = 1250.5\n"
                "active = True\n\n"
                "print(username, level, xp, active)\n"
            ),
            "challenge": "Create variables `item = 'Keyboard'` and `price = 79.99`. Print both on one line.",
            "solution": "item = 'Keyboard'\nprice = 79.99\nprint(item, price)",
        },
        "typecasting": {
            "theory": (
                "### Typecasting\n\n"
                "Explicit conversion between types:\n"
                "- `int()`: converts to integer\n"
                "- `float()`: converts to float\n"
                "- `str()`: converts to string\n"
                "- `bool()`: `0`, `''`, `None`, and `[]` evaluate to `False`; all else is `True`.\n"
            ),
            "demo_code": (
                "text_num = '150'\n"
                "num = int(text_num)\n"
                "print('Total:', num + 50)\n"
                "print('bool(0):', bool(0))\n"
                "print('bool(\"test\"):', bool('test'))\n"
            ),
            "challenge": "Convert string '24.5' to float, add 5.5, and print the result.",
            "solution": "val = float('24.5')\nprint(val + 5.5)",
        },
        "f-strings": {
            "theory": (
                "### f-strings\n\n"
                "Prefix string with `f` to embed expressions in `{}`:\n"
                "- Float precision: `{price:.2f}`\n"
                "- Math calculations: `{a + b}`\n"
                "- Debug shorthand: `{var=}`\n"
            ),
            "demo_code": (
                "product = 'Mouse'\n"
                "price = 29.99\n"
                "tax = 0.08\n\n"
                "print(f'Item: {product}')\n"
                "print(f'Final Price: ${price * (1 + tax):.2f}')\n"
            ),
            "challenge": "Given `val = 12.3456`, print 'Result: 12.35' rounded to 2 decimals using an f-string.",
            "solution": "val = 12.3456\nprint(f'Result: {val:.2f}')",
        },
        "if-elif-else": {
            "theory": (
                "### Conditionals\n\n"
                "Branching execution using `if`, `elif`, and `else`.\n"
                "Supports logical operators `and`, `or`, and `not`.\n"
            ),
            "demo_code": (
                "score = 85\n\n"
                "if score >= 90:\n"
                "    print('Grade: A')\n"
                "elif score >= 80:\n"
                "    print('Grade: B')\n"
                "else:\n"
                "    print('Grade: C or below')\n"
            ),
            "challenge": "If `x = 10` is greater than 0, print 'Positive', else print 'Non-positive'.",
            "solution": "x = 10\nif x > 0:\n    print('Positive')\nelse:\n    print('Non-positive')",
        },
        "match-function": {
            "theory": (
                "### match-case\n\n"
                "Introduced in Python 3.10 for pattern matching:\n"
                "- `case val:` match pattern\n"
                "- `case a | b:` match either pattern\n"
                "- `case _:` default catch-all\n"
            ),
            "demo_code": (
                "status = 200\n\n"
                "match status:\n"
                "    case 200:\n"
                "        print('OK')\n"
                "    case 404:\n"
                "        print('Not Found')\n"
                "    case _:\n"
                "        print('Other Status')\n"
            ),
            "challenge": "Match `cmd = 'stop'`. Print 'Stopping' on 'stop' and 'Starting' on 'start'.",
            "solution": "cmd = 'stop'\nmatch cmd:\n    case 'start':\n        print('Starting')\n    case 'stop':\n        print('Stopping')",
        },
        "for loop": {
            "theory": (
                "### for Loop\n\n"
                "Iterates over iterables or a `range()` sequence.\n"
                "- `range(start, stop[, step])`\n"
            ),
            "demo_code": (
                "for i in range(1, 5):\n"
                "    print(f'Count: {i}')\n\n"
                "for letter in 'Dev':\n"
                "    print(f'Letter: {letter}')\n"
            ),
            "challenge": "Sum numbers from 1 to 5 with a for loop and print the total.",
            "solution": "total = 0\nfor i in range(1, 6):\n    total += i\nprint(total)",
        },
        "while loop": {
            "theory": (
                "### while Loop\n\n"
                "Repeats execution as long as condition evaluates to `True`.\n"
            ),
            "demo_code": (
                "counter = 3\n"
                "while counter > 0:\n"
                "    print('Countdown:', counter)\n"
                "    counter -= 1\n"
                "print('Blastoff!')\n"
            ),
            "challenge": "Use a while loop to print numbers from 1 to 3.",
            "solution": "n = 1\nwhile n <= 3:\n    print(n)\n    n += 1",
        },
        "break, continue, pass statements": {
            "theory": (
                "### Loop Controls\n\n"
                "- `break`: Terminate loop completely.\n"
                "- `continue`: Skip immediately to next iteration.\n"
                "- `pass`: Placeholder that does nothing.\n"
            ),
            "demo_code": (
                "for n in range(1, 6):\n"
                "    if n == 2:\n"
                "        continue  # skip 2\n"
                "    if n == 5:\n"
                "        break     # stop at 5\n"
                "    print(n)\n"
            ),
            "challenge": "Loop range(1, 6). Skip number 3 using continue and print the others.",
            "solution": "for n in range(1, 6):\n    if n == 3:\n        continue\n    print(n)",
        },
    },
    "Section 3: Advanced Datatypes": {
        "list": {
            "theory": (
                "### Lists\n\n"
                "Ordered, mutable collections that allow duplicates.\n"
                "- Indexing: `lst[0]`, `lst[-1]`\n"
                "- Mutability: `lst[0] = new_val`\n"
            ),
            "demo_code": (
                "items = ['A', 'B', 'C']\n"
                "print('First:', items[0])\n"
                "items[0] = 'Alpha'\n"
                "print('Updated:', items)\n"
            ),
            "challenge": "Given `lst = [10, 20, 30]`, change index 0 to 99 and print `lst`.",
            "solution": "lst = [10, 20, 30]\nlst[0] = 99\nprint(lst)",
        },
        "list function": {
            "theory": (
                "### List Methods\n\n"
                "- `.append(x)`: Adds item to end\n"
                "- `.pop()`: Removes and returns last item\n"
                "- `.sort()`: Sorts list in-place\n"
            ),
            "demo_code": (
                "nums = [3, 1, 2]\n"
                "nums.append(4)\n"
                "nums.sort()\n"
                "print('Sorted:', nums)\n"
                "print('Popped:', nums.pop())\n"
            ),
            "challenge": "Sort `[4, 2, 1]`, append 5, and print it.",
            "solution": "lst = [4, 2, 1]\nlst.sort()\nlst.append(5)\nprint(lst)",
        },
        "tuple": {
            "theory": (
                "### Tuples\n\n"
                "Ordered and **immutable** sequences.\n"
                "- Cannot be modified after creation.\n"
                "- Supports unpacking: `a, b = my_tuple`.\n"
            ),
            "demo_code": (
                "point = (10, 20)\n"
                "print('X:', point[0])\n"
                "x, y = point\n"
                "print(f'Unpacked: {x=}, {y=}')\n"
            ),
            "challenge": "Create tuple `t = (1, 2)`. Unpack into `a, b` and print `b`.",
            "solution": "t = (1, 2)\na, b = t\nprint(b)",
        },
        "tuple functions": {
            "theory": (
                "### Tuple Functions\n\n"
                "- `.count(x)`: Number of occurrences\n"
                "- `.index(x)`: First index of item\n"
                "- Built-ins: `len()`, `min()`, `max()`, `sum()`\n"
            ),
            "demo_code": (
                "t = (1, 2, 2, 3)\n"
                "print('Count of 2:', t.count(2))\n"
                "print('Index of 3:', t.index(3))\n"
            ),
            "challenge": "Given `vals = (5, 10, 5)`, print how many times 5 appears.",
            "solution": "vals = (5, 10, 5)\nprint(vals.count(5))",
        },
        "set": {
            "theory": (
                "### Sets\n\n"
                "Unordered collections of unique items.\n"
                "- Automatically discards duplicates.\n"
                "- O(1) membership testing (`x in my_set`).\n"
            ),
            "demo_code": (
                "s = {1, 2, 2, 3}\n"
                "print('Set contents:', s)\n"
                "print('Is 2 in set:', 2 in s)\n"
            ),
            "challenge": "Convert `[1, 1, 2, 3]` to a set and print it.",
            "solution": "print(set([1, 1, 2, 3]))",
        },
        "set functions": {
            "theory": (
                "### Set Operations\n\n"
                "- Union (`|`): Items in either set\n"
                "- Intersection (`&`): Items in both sets\n"
                "- Difference (`-`): In first set but not second\n"
            ),
            "demo_code": (
                "a = {1, 2, 3}\n"
                "b = {2, 3, 4}\n"
                "print('Union:', a | b)\n"
                "print('Intersection:', a & b)\n"
                "print('Difference:', a - b)\n"
            ),
            "challenge": "Given `a = {'cat', 'dog'}` and `b = {'dog'}`, print intersection using `&`.",
            "solution": "a = {'cat', 'dog'}\nb = {'dog'}\nprint(a & b)",
        },
        "dictionary": {
            "theory": (
                "### Dictionaries\n\n"
                "Stores `key: value` pairings.\n"
                "- Keys must be unique and immutable.\n"
                "- Fast lookups: $O(1)$ average time.\n"
            ),
            "demo_code": (
                "user = {'name': 'Sam', 'role': 'Admin'}\n"
                "print('Name:', user['name'])\n"
                "user['active'] = True\n"
                "print('User Dict:', user)\n"
            ),
            "challenge": "Create dictionary with key 'lang' equal to 'Python'. Print value of 'lang'.",
            "solution": "d = {'lang': 'Python'}\nprint(d['lang'])",
        },
        "dictionary functions": {
            "theory": (
                "### Dictionary Methods\n\n"
                "- `.get(key, default)`: Safe retrieval without key error\n"
                "- `.keys()`, `.values()`, `.items()`: Iterable views\n"
            ),
            "demo_code": (
                "info = {'host': 'localhost'}\n"
                "print('Port (default):', info.get('port', 8080))\n"
                "for k, v in info.items():\n"
                "    print(f'{k} = {v}')\n"
            ),
            "challenge": "Given `d = {'a': 1}`, use `.get()` to lookup 'b' with default 0 and print it.",
            "solution": "d = {'a': 1}\nprint(d.get('b', 0))",
        },
    },
    "Section 4: Functions and all about them": {
        "declaring a function": {
            "theory": (
                "### Functions\n\n"
                "Reusable blocks declared with `def` keyword.\n"
            ),
            "demo_code": (
                "def add(a: int, b: int) -> int:\n"
                "    return a + b\n\n"
                "print('Result:', add(5, 7))\n"
            ),
            "challenge": "Write a function `square(x)` returning $x^2$. Call with 4 and print.",
            "solution": "def square(x):\n    return x * x\nprint(square(4))",
        },
        "*args": {
            "theory": (
                "### *args\n\n"
                "Accepts arbitrary positional arguments collected as a tuple.\n"
            ),
            "demo_code": (
                "def total(*nums):\n"
                "    return sum(nums)\n\n"
                "print('Sum:', total(10, 20, 30))\n"
            ),
            "challenge": "Write `sum_all(*args)` that returns the sum of arguments. Call with 1, 2, 3 and print.",
            "solution": "def sum_all(*args):\n    return sum(args)\nprint(sum_all(1, 2, 3))",
        },
        "**kwargs": {
            "theory": (
                "### **kwargs\n\n"
                "Accepts arbitrary named keyword arguments collected as a dictionary.\n"
            ),
            "demo_code": (
                "def display(**kwargs):\n"
                "    for k, v in kwargs.items():\n"
                "        print(f'{k}: {v}')\n\n"
                "display(lang='Python', version=3.12)\n"
            ),
            "challenge": "Write `print_keys(**kwargs)` that prints keys in kwargs. Call with `a=1`.",
            "solution": "def print_keys(**kwargs):\n    for k in kwargs:\n        print(k)\nprint_keys(a=1)",
        },
        "decorators": {
            "theory": (
                "### Decorators\n\n"
                "Functions that modify the behavior of another function using `@`.\n"
            ),
            "demo_code": (
                "def banner(func):\n"
                "    def wrapper():\n"
                "        print('--- START ---')\n"
                "        func()\n"
                "        print('--- END ---')\n"
                "    return wrapper\n\n"
                "@banner\n"
                "def say_hello():\n"
                "    print('Hello World!')\n\n"
                "say_hello()\n"
            ),
            "challenge": "Create a decorator `loud` that prints 'START' before and 'END' after calling `func()`. Test on a function printing 'OK'.",
            "solution": "def loud(func):\n    def wrapper():\n        print('START')\n        func()\n        print('END')\n    return wrapper\n\n@loud\ndef run():\n    print('OK')\nrun()",
        },
    },
    "Section 5: Object oriented programming": {
        "OOPs part 1": {
            "theory": (
                "### Classes and Objects\n\n"
                "Encapsulates state (attributes) and behavior (methods).\n"
                "- `__init__(self, ...)` constructor initializes instance state.\n"
            ),
            "demo_code": (
                "class User:\n"
                "    def __init__(self, username):\n"
                "        self.username = username\n\n"
                "    def greet(self):\n"
                "        return f'Hello, {self.username}!'\n\n"
                "u = User('Alex')\n"
                "print(u.greet())\n"
            ),
            "challenge": "Create class `Dog` with `name` in `__init__`. Instantiate with 'Buddy' and print the name.",
            "solution": "class Dog:\n    def __init__(self, name):\n        self.name = name\nd = Dog('Buddy')\nprint(d.name)",
        },
        "OOPs part 2": {
            "theory": (
                "### Inheritance & Polymorphism\n\n"
                "- Child inherits from parent: `class Child(Parent):`\n"
                "- Overriding: Methods can provide specialized implementations.\n"
            ),
            "demo_code": (
                "class Animal:\n"
                "    def sound(self):\n"
                "        return 'Some sound'\n\n"
                "class Cat(Animal):\n"
                "    def sound(self):\n"
                "        return 'Meow!'\n\n"
                "c = Cat()\n"
                "print(c.sound())\n"
            ),
            "challenge": "Create base `Shape` with `draw()` returning 'Shape'. Child `Box` overrides to return 'Box'. Print `Box().draw()`.",
            "solution": "class Shape:\n    def draw(self):\n        return 'Shape'\nclass Box(Shape):\n    def draw(self):\n        return 'Box'\nprint(Box().draw())",
        },
    },
}