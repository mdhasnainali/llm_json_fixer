# main.py
import argparse
import sys
from llm_json_fixer import fix_json

def main():
    parser = argparse.ArgumentParser(
        description="Fix malformed JSON from LLM outputs."
    )
    parser.add_argument(
        "input",
        type=str,
        help="The malformed JSON string to fix. You can also use @filename.json to read from a file.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed fix info and intermediate states.",
    )
    args = parser.parse_args()

    # Allow reading from a file
    if args.input.startswith("@"):
        try:
            with open(args.input[1:], "r", encoding="utf-8") as f:
                input_text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.input[1:]}' not found.")
            sys.exit(1)
    else:
        input_text = args.input

    result = fix_json(input_text, return_dict=True)

    if result["success"]:
        print("✅ Fixed JSON:")
        print(result["data"])
        if args.verbose:
            print("\n🛠 Fixes Applied:")
            for fix in result["fixes_applied"]:
                print(" -", fix)
    else:
        print("❌ Failed to fix JSON:")
        print("Error:", result["error"])
        if args.verbose and result["fixes_applied"]:
            print("\n🛠 Fixes Attempted:")
            for fix in result["fixes_applied"]:
                print(" -", fix)

if __name__ == "__main__":
    main()
