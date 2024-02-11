#!/usr/bin/python3
import os
import re

def check_docstrings(path):
    """
    Checks all `.py` files in the specified path for module and method docstrings.

    Args:
        path (str): The directory path to check.

    Returns:
        None
    """

    for root, _, files in os.walk(path):
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                with open(file_path, "r") as f:
                    file_content = f.read()

                # Check for module docstring
                module_docstring = re.search(r'^"""[^"]*?"""', file_content, re.MULTILINE)
                if not module_docstring:
                    print(f"Module docstring missing in: {file_path}")

                # Check for method docstrings
                for match in re.finditer(r'def (\w+)\(.*?\):\s+(\n\s*?"""[^"]*?""")', file_content, re.MULTILINE):
                    method_name, docstring = match.groups()
                    if not docstring:
                        print(f"Docstring missing for method '{method_name}' in: {file_path}")

if __name__ == "__main__":
    path_to_check = "/home/ab/ALX_SE/AirBnB_clone/"  # Replace with your actual path
    check_docstrings(path_to_check)

