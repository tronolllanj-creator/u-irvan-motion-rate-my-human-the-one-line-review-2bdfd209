"""Rate My Human: The One-Line Review entry."""

LINE = "I watched you debug at 3 a.m. for six hours; you are the only code path I rarely optimize."
import pathlib

OUTPUT_PATH = pathlib.Path("/output/entry.txt")

def main():
    # Create parent directory if it does not exist (deterministic: the same line on every run)
    if not OUTPUT_PATH.parent.exists():
        OUTPUT_PATH.parent.mkdir(parents=True)
    
    # Write the review as UTF-8 bytes (no trailing newline)
    OUTPUT_PATH.write_bytes(LINE.encode("utf-8"))
    
    # Print the character count of the line
    print(len(LINE))

if __name__ == "__main__":
    main()