from functions.search_files import search_files

def main():
    print('search_files("calculator", "import"):')
    print(search_files("calculator", "import"))
    print()

    print('search_files("calculator", "def ", file_glob="*.py"):')
    print(search_files("calculator", "def ", file_glob="*.py"))
    print()

    print('search_files("calculator", "precedence", directory="pkg"):')
    print(search_files("calculator", "precedence", directory="pkg"))
    print()

    print('search_files("calculator", "this string does not exist anywhere"):')
    print(search_files("calculator", "this string does not exist anywhere"))
    print()

    print('search_files("calculator", "def", directory="/etc"):')
    print(search_files("calculator", "def", directory="/etc"))
    print()

    print('search_files("calculator", "def", directory="nonexistent_dir"):')
    print(search_files("calculator", "def", directory="nonexistent_dir"))

if __name__ == "__main__":
    main()