import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not found. Please set it in your .env file.")

    client = genai.Client(api_key=api_key)

    for _ in range(20):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
                temperature=0,
            ),
        )

        if args.verbose:
            try:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            except RuntimeError:
                print("Token usage information is not available for this response.")

        # Append model's candidates to message history
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        # No function calls — final response
        if not response.function_calls:
            print("Final response:")
            print(response.text)
            return

        # Handle function calls
        function_responses = []
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)

            if not function_call_result.parts:
                raise Exception("No parts in function call result")
            if function_call_result.parts[0].function_response is None:
                raise Exception("No function response in result")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("No response data in function response")

            function_responses.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        # Append tool results to message history
        messages.append(types.Content(role="user", parts=function_responses))

    print("Error: maximum iterations reached without a final response.")
    exit(1)


if __name__ == "__main__":
    main()