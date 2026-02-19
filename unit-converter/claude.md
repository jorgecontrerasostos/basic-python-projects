# Python Fundamentals Practice - Claude Guide

## How to Use This Guide

This file helps you work through Python projects systematically **without giving you the code**. When you're stuck, ask Claude to:

- Break down the current task into smaller steps
- Explain concepts you don't understand
- Point you toward relevant documentation
- Review your approach (without writing code for you)
- Help debug by asking questions about your logic

**What Claude WON'T do:** Write complete solutions, give you code snippets unprompted, or solve problems for you.

---

## General Problem-Solving Framework

For any project, follow this approach:

### 1. Understand the Requirements
- What are the inputs?
- What are the expected outputs?
- What edge cases should you handle?
- What Python fundamentals does this project practice?

### 2. Break Down the Problem
- List the major features/functions needed
- Identify which parts depend on others
- Start with the simplest piece first

### 3. Plan Your Data Structures
- What data types make sense? (lists, dicts, sets, tuples)
- How will you organize information?
- What needs to persist between runs?

### 4. Implement Incrementally
- Build one small piece at a time
- Test each piece before moving forward
- Don't try to build everything at once

### 5. Handle Edge Cases
- What happens with invalid input?
- What if files don't exist?
- What if data is malformed?

---

## Python Best Practices

### Code Style and Readability

**PEP 8 Compliance:**
- Follow Python's official style guide for consistent, readable code
- Use 4 spaces for indentation (never tabs)
- Limit lines to 79-88 characters when reasonable
- Use meaningful variable and function names (`calculate_total` not `calc_tot`)
- Follow naming conventions: `snake_case` for functions/variables, `PascalCase` for classes, `UPPER_CASE` for constants

**Readable Code Principles:**
- Write code that explains itself — minimize the need for comments
- Keep functions small and focused (one responsibility per function)
- Avoid deep nesting — flatten when possible using early returns or guard clauses
- Use whitespace to separate logical blocks
- Prefer explicit over implicit (be clear about what your code does)

---

## When to Use Object-Oriented Programming

**Use classes when you have:**
- Data with associated behaviors (a Contact has name/phone AND methods to validate/format)
- Multiple instances of the same concept (many Student objects, each with their own data)
- State that needs to be maintained and modified over time
- Complex entities that benefit from encapsulation

**Avoid classes when:**
- You just need to group related functions (use a module instead)
- Your class only has one method besides `__init__` (probably just needs a function)
- Simple scripts or utilities that don't model real-world entities
- You're forcing OOP where procedural code is clearer

**Key OOP principles to practice:**
- **Encapsulation:** Keep related data and methods together, hide internal details
- **Single Responsibility:** Each class should have one clear purpose
- **Composition over inheritance:** Prefer building complex objects from simpler ones
- Don't over-engineer — start simple and refactor to OOP when you feel the pain of not having it

---

## Documentation with Docstrings

**Always write docstrings for:**
- Modules (at the top of .py files)
- Classes (describing what the class represents)
- Public functions and methods (not necessarily private/helper ones)

**Docstring format (Google style recommended):**

```python
def function_name(param1: int, param2: str) -> bool:
    """
    Brief one-line description of what the function does.
    
    More detailed explanation if needed, describing the purpose,
    behavior, or any important considerations.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When invalid input is provided
    """
```

**Tips:**
- Start with a concise one-liner that fits on one line
- Add details below if the function is complex
- Document parameters, return values, and exceptions
- Update docstrings when you change function behavior
- Keep docstrings accurate — outdated docs are worse than none

---

## Writing Pythonic Code

**Embrace Python idioms:**

**Iterate directly over collections:**
- Instead of indexing, loop over items directly
- Use `enumerate()` when you need both index and value
- Use `zip()` to iterate over multiple sequences together

**Use list/dict/set comprehensions:**
- More concise and often faster than loops
- Keep them simple — if too complex, use a regular loop
- Generator expressions for large datasets

**Context managers for resources:**
- Always use `with` statement for files, connections, locks
- Ensures proper cleanup even if errors occur

**Truthiness and None checks:**
- Use `if my_list:` instead of `if len(my_list) > 0:`
- Use `if value is None:` instead of `if value == None:`

**Multiple assignment and unpacking:**
- `x, y = 1, 2` or `first, *rest = my_list`
- Great for returning multiple values from functions

**Dictionary methods:**
- Use `.get()` with defaults instead of checking key existence
- Use `.setdefault()` or `defaultdict` for accumulators

**String formatting:**
- Prefer f-strings: `f"Hello {name}"` (Python 3.6+)
- Use `.join()` for concatenating many strings

---

## Clean Code Practices

**Functions:**
- Keep them short (ideally under 20-30 lines)
- One clear purpose per function
- Minimize side effects — prefer pure functions when possible
- Return early to reduce nesting

**Error Handling:**
- Use exceptions for exceptional cases, not control flow
- Be specific with exception types (catch `FileNotFoundError`, not bare `Exception`)
- Include helpful error messages
- Clean up resources in `finally` blocks or use context managers

**Don't Repeat Yourself (DRY):**
- Extract repeated logic into functions
- Use loops and comprehensions instead of copy-paste
- Create helper functions for common patterns

**Configuration and Magic Numbers:**
- Define constants at the module level for values used multiple times
- Use descriptive names: `MAX_RETRIES = 3` not just `3` in code
- Consider config files for user-adjustable settings

**Separation of Concerns:**
- Business logic separate from I/O operations
- Data processing separate from presentation
- Keep main execution flow in an `if __name__ == "__main__":` block

---

## Dependency Management

**Always use a virtual environment:**
- `python -m venv venv` for project isolation
- Activate before installing packages
- Keeps system Python clean

**Modern alternative - uv (recommended):**
- `uv` is a fast, modern Python package and project manager written in Rust
- **Much faster** than pip (10-100x in many cases)
- Built-in virtual environment management
- Better dependency resolution
- Compatible with pip and PyPI

**Getting started with uv:**
```shell
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a new project with virtual environment
uv init my-project
cd my-project

# Add dependencies (automatically manages venv)
uv add requests
uv add pytest --dev

# Run Python scripts
uv run python main.py

# Sync dependencies from pyproject.toml
uv sync
```

**Traditional pip approach:**
```shell
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install requests==2.31.0
pip freeze > requirements.txt
```

**Pin your dependencies:**
- **With uv:** Dependencies automatically tracked in `pyproject.toml` and `uv.lock`
- **With pip:** Create and maintain a `requirements.txt` file
- Pin specific versions: `requests==2.31.0`
- Use `pip freeze > requirements.txt` to capture current environment
- Document Python version requirement (e.g., "Requires Python 3.8+")

**Choose stable, maintained libraries:**
- Check last update date and GitHub activity
- Read documentation quality and community size
- Prefer libraries with semantic versioning
- Avoid libraries with known security vulnerabilities

**Version compatibility:**
- Test your code against the Python versions you claim to support
- Be aware of deprecation warnings
- Keep dependencies updated, but test after updates

**Common stable libraries for fundamentals:**
- `requests` for HTTP (pinned versions, e.g., `==2.31.0`)
- `pytest` for testing
- `ruff` for fast linting and formatting (modern alternative)
- `black` for code formatting (traditional option)
- `pylint` or `flake8` for linting (traditional options)

---

## Code Organization

**Project structure:**
```
project_name/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
└── data/ (if needed)
```

**Module organization:**
- Group related functionality into modules
- Keep files focused and reasonably sized (under 500 lines ideally)
- Use `__init__.py` to make directories into packages
- Avoid circular imports by careful design

---

## Testing Mindset

**Write tests for:**
- Core business logic
- Edge cases and boundary conditions
- Error handling paths

**Basic testing approach:**
- Start with simple assertions
- Test one thing per test function
- Use descriptive test names that explain what's being tested
- Aim for tests that are easy to read and maintain

**When to test:**
- After implementing a feature
- Before fixing a bug (write a failing test first)
- When refactoring (ensure tests still pass)

---

## Type Hints (Python 3.5+)

**Benefits of type hints:**
- Catch bugs earlier with static type checkers (mypy)
- Improve IDE autocomplete and suggestions
- Serve as inline documentation
- Make refactoring safer

**Basic type hints:**
```python
def calculate_average(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

name: str = "Jorge"
age: int = 25
scores: dict[str, int] = {"math": 95, "history": 87}
```

**When to use:**
- Function parameters and return values (always recommended)
- Class attributes when type isn't obvious
- Module-level variables when ambiguous

**When to skip:**
- Simple scripts or one-off tasks
- When types are obvious from context
- Don't go overboard — use when it adds clarity

---

## Logging Instead of Print Statements

**Why logging over print:**
- Control verbosity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Easy to disable or redirect output
- Include timestamps and module information automatically
- Professional standard for production code

**Basic logging setup:**
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.debug("Detailed diagnostic information")
logger.info("General informational messages")
logger.warning("Warning messages")
logger.error("Error messages")
logger.critical("Critical issues")
```

**When to use:**
- Any application that might need debugging
- Programs that run unattended
- When you need to track program flow
- For production-ready code

**Use print() only for:**
- Quick debugging during development
- Scripts where output IS the product (like reports)
- Interactive programs with user-facing output

---

## Performance Considerations

**Premature optimization is bad, but be aware:**

**Use appropriate data structures:**
- Lists for ordered collections with frequent appends
- Sets for membership testing (much faster than lists)
- Dictionaries for key-value lookups
- Tuples for immutable sequences

**Avoid common pitfalls:**
- Don't repeatedly concatenate strings in loops (use join or f-strings)
- Don't check `if item in long_list` repeatedly (convert to set)
- Don't load entire large files into memory if you can process line-by-line
- Generator expressions over list comprehensions for large datasets

**Profile before optimizing:**
- Use `time` module to measure execution time
- Use `cProfile` for detailed profiling
- Optimize the bottleneck, not everything

**Remember:** Readable code > Clever code. Only optimize when you have a real performance problem.

---

## Security Best Practices

**Never hardcode secrets:**
- Use environment variables for API keys, passwords, database URLs
- Use `.env` files with `python-dotenv` library (never commit .env to git)
- Add sensitive files to `.gitignore`

**Input validation:**
- Validate and sanitize all user input
- Don't trust external data sources
- Use type checking and range validation
- Be careful with `eval()` — avoid it almost always

**File operations:**
- Validate file paths to prevent directory traversal attacks
- Check file sizes before reading to prevent memory issues
- Be cautious with `pickle` — never unpickle untrusted data

**Dependencies:**
- Regularly update dependencies to patch security issues
- Use `pip-audit` or similar tools to check for vulnerabilities
- Be cautious with unmaintained libraries

---

## Git Best Practices for Python Projects

**Always include:**
- `.gitignore` file (use Python template from GitHub)
- Ignore: `venv/`, `__pycache__/`, `*.pyc`, `.env`, `.DS_Store`
- `README.md` with setup instructions
- `requirements.txt` for dependencies

**Commit practices:**
- Small, focused commits
- Clear, descriptive commit messages
- Don't commit secrets, API keys, or credentials
- Don't commit virtual environments or compiled files
- Test code before committing

**Branch workflow:**
- Keep `main` branch stable
- Use feature branches for new work
- Meaningful branch names: `feature/user-authentication` not `fix-stuff`

---

## Common Python Gotchas to Avoid

**Mutable default arguments:**
- Don't use mutable defaults like `def func(items=[]):` — use `None` instead
- Lists, dicts, and sets as defaults are shared across calls

**Late binding in closures:**
- Variables in loops can cause unexpected behavior in nested functions
- Use function parameters to capture values properly

**Shallow vs deep copy:**
- `list.copy()` and `dict.copy()` only copy the top level
- Nested structures need `copy.deepcopy()` for true duplication

**Integer caching:**
- Small integers (-5 to 256) are cached by Python
- `is` vs `==` behaves differently for different integer ranges

**Global variables:**
- Avoid when possible — hard to test and debug
- If needed, be explicit with `global` keyword
- Better: pass values as parameters

---

## Continuous Improvement

**Tools to level up:**

**Modern Python toolchain (recommended):**
- **ruff**: Extremely fast linter and formatter (replaces flake8, pylint, black, isort)
  - 10-100x faster than traditional tools
  - Combines multiple tools into one
  - Easy configuration via `pyproject.toml`
  - Run with: `ruff check .` and `ruff format .`
- **uv**: Fast package manager (replaces pip + venv management)
- **mypy**: Static type checking
- **pytest**: Better testing framework than unittest
- **ipython**: Enhanced interactive shell for experimentation

**Traditional Python toolchain:**
- **black** or **autopep8**: Automatic code formatting
- **pylint** or **flake8**: Catch style issues and potential bugs
- **mypy**: Static type checking
- **pytest**: Testing framework
- **ipython**: Enhanced interactive shell

**Quick setup with Ruff:**
```shell
# Install
uv add ruff --dev  # or: pip install ruff

# Check for issues
ruff check .

# Auto-fix issues
ruff check . --fix

# Format code
ruff format .

# Add to pyproject.toml for configuration
[tool.ruff]
line-length = 88
target-version = "py38"
```

**Learning resources:**
- Python official documentation (docs.python.org)
- Real Python tutorials
- PEP 8 style guide (peps.python.org/pep-0008)
- "Effective Python" and "Fluent Python" books
- Ruff documentation (docs.astral.sh/ruff)

**Code review checklist:**
- Does it follow PEP 8? (Run `ruff check .`)
- Are functions small and focused?
- Are names clear and descriptive?
- Is error handling appropriate?
- Are there docstrings for public APIs?
- Could this be simpler?

---

## When You Get Stuck

Ask Claude questions like:
- "What Python data structure should I use for storing X?"
- "How do I approach breaking down this feature?"
- "Can you explain how [concept] works without showing me code?"
- "I'm getting [error], what category of problem is this?"
- "What should I research to understand [topic] better?"
- "Is my approach reasonable, or is there a simpler way to think about this?"

## Remember

The goal isn't to finish fast — it's to **build your problem-solving muscles**. Struggle a bit before asking for help. Write messy code first, then refactor. Make mistakes and debug them yourself.

You've got this! 🚀