"""One-line joke entry for make.fun: The Meeting That Should Have Been an Email.

Writes a single line of plain text (the entry) to the output file, with no
trailing newline. Python standard library only.
"""

import os

LINE = "The follow-up email began 'As discussed' — nothing was discussed."


def resolve_output_path():
    path = os.environ.get("ENTRY_OUTPUT")
    if path:
        return path
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    path = resolve_output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
