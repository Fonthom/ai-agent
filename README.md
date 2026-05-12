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

## Project Structure

- `main.py` — CLI entry point for running the chatbot with a user prompt.
- `call_function.py` — dispatches tool calls from the model to local Python helpers.
- `prompts.py` — contains the system prompt that defines the AI’s behavior.
- `functions/` — tool implementations and their Gemini function schemas.
- `calculator/` — sample code and data used by the functions.
- `test_*.py` — unit tests validating the helper functions and search behavior.

## Requirements

- Python 3.13 or newer
- `google-genai==1.12.1`
- `python-dotenv==1.1.0`

## Setup

1. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist, install directly:

```bash
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

3. Create a `.env` file in the repository root with your Gemini API key:

```bash
GEMINI_API_KEY=your_api_key_here
```

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

## Testing

Run the project tests with:

```bash
python -m pytest
```

The test suite covers the helper functions and ensures search and file access behaviors work as expected.

## Security Notes

- The current implementation is intended for education and experimentation.
- File operations are restricted to `./calculator`, but the code does not include full production-level sandboxing.
- Use caution before adding or exposing this project in a real application.

## Extending the Project

To add a new tool:

1. Create a new schema and function implementation in `functions/`.
2. Register the function in `call_function.py` and `available_functions`.
3. Update the system prompt in `prompts.py` if needed.

## License

This project is a simple educational example. No license is specified.
