import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "functions"))

from run_python_file import run_python_file

print("=" * 60)
print("Test 1: Run calculator with no args (should show usage)")
print("=" * 60)
result = run_python_file("calculator", "main.py")
print(result)

print()
print("=" * 60)
print("Test 2: Run calculator with expression '3 + 5'")
print("=" * 60)
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(result)

print()
print("=" * 60)
print("Test 3: Run calculator tests (should all pass)")
print("=" * 60)
result = run_python_file("calculator", "tests.py")
print(result)

print()
print("=" * 60)
print("Test 4: Path outside working directory (should error)")
print("=" * 60)
result = run_python_file("calculator", "../main.py")
print(result)

print()
print("=" * 60)
print("Test 5: Nonexistent file (should error)")
print("=" * 60)
result = run_python_file("calculator", "nonexistent.py")
print(result)

print()
print("=" * 60)
print("Test 6: Non-Python file (should error)")
print("=" * 60)
result = run_python_file("calculator", "lorem.txt")
print(result)