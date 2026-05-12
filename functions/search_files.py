import os
import fnmatch
from google.genai import types

schema_search_files = types.FunctionDeclaration(
    name="search_files",
    description="Searches for a string pattern in files within a directory, returns matching lines with file names and line numbers",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "pattern": types.Schema(
                type=types.Type.STRING,
                description="The string pattern to search for",
            ),
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory to search in, relative to the working directory (default is working directory)",
            ),
            "file_glob": types.Schema(
                type=types.Type.STRING,
                description="Optional glob pattern to filter files, e.g. '*.py' (default is all files)",
            ),
        },
        required=["pattern"],
    ),
)

MAX_RESULTS = 50

def search_files(working_directory, pattern, directory=".", file_glob="*"):
    try:
        working_dir_abs = os.path.abspath(os.path.join(os.getcwd(), working_directory))
        search_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if os.path.commonpath([working_dir_abs, search_dir]) != working_dir_abs:
            return f'Error: Cannot search "{directory}" as it is outside the permitted working directory'

        results = []
        for root, _, files in os.walk(search_dir):
            for filename in files:
                if not fnmatch.fnmatch(filename, file_glob):
                    continue
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, "r") as f:
                        for i, line in enumerate(f, 1):
                            if pattern in line:
                                rel_path = os.path.relpath(filepath, working_dir_abs)
                                results.append(f"{rel_path}:{i}: {line.rstrip()}")
                                if len(results) >= MAX_RESULTS:
                                    results.append(f"[truncated at {MAX_RESULTS} results]")
                                    return "\n".join(results)
                except Exception:
                    continue

        return "\n".join(results) if results else f"No matches found for '{pattern}'"

    except Exception as e:
        return f"Error: {e}"