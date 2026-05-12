# AI Agent

A lightweight Python project that demonstrates a function-calling AI assistant built on Google Gemini. The assistant can inspect files, search code, execute Python scripts, and write files in a restricted working directory.

## Features

- Uses `google-genai` to interact with Gemini models.
- Supports tool-enabled function calls via `available_functions`.
- Includes helper functions for:
  - listing files and directories
  - reading file content
  - searching text in files
  - executing Python files
  - writing files
- Limits operations to a curated working directory (`./calculator`).

## Usage

Run the chatbot from the command line with a prompt:

```bash
python main.py "Show me all Python files in the calculator directory"
```

Add `--verbose` for extra debug output:

```bash
python main.py "Inspect the calculator package" --verbose
```

## How It Works

1. `main.py` loads the Gemini API key from `.env`.
2. It sends the user prompt to Gemini with a system instruction from `prompts.py`.
3. Gemini may return a function call instead of a final answer.
4. `call_function.py` maps the function call to a local helper in `functions/`.
5. Results are returned to Gemini, which may then produce a final response.

## Available Tools

- `get_files_info(directory)` — list files in a directory.
- `get_file_content(file_path)` — read a file’s content.
- `search_files(pattern, directory, file_glob)` — search files for a pattern.
- `run_python_file(file_path, args)` — execute a Python file and capture output.
- `write_file(file_path, content)` — create or overwrite a file.

## Security Notes

- The current implementation is intended for education and experimentation.
- File operations are restricted to `./calculator`, but the code does not include full production-level sandboxing.
- Use caution before adding or exposing this project in a real application.



