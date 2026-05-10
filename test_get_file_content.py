from functions.get_file_content import get_file_content

def main():
    print('get_file_content("calculator", "lorem.txt"):')
    result = get_file_content("calculator", "lorem.txt")
    print(f"  Length: {len(result)} characters")
    truncation_msg = '[...File "lorem.txt" truncated at 10000 characters]'
    print(f"  Truncated: {truncation_msg in result}")
    print()

    print('get_file_content("calculator", "main.py"):')
    print(get_file_content("calculator", "main.py"))
    print()

    print('get_file_content("calculator", "pkg/calculator.py"):')
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    print('get_file_content("calculator", "/bin/cat"):')
    print(get_file_content("calculator", "/bin/cat"))
    print()

    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()