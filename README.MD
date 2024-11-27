# Random Line Retriever

This script allows you to efficiently retrieve an arbitrary line from a plain text file.
The script uses an index file to store the byte offsets of each line, enabling quick access to any line in the file.

## Features

- Efficiently retrieves an arbitrary line from a text file.
- Uses an index file to store byte offsets for quick access.
- Handles both the creation and reading of the index file.
- Supports displaying the contents of the index file.

## Requirements

- Python 3.x

## Usage

### Retrieve a Specific Line

To retrieve a specific line from the input file, use the following command:

    python process_file.py <file_path> <line_index>

    <file_path>: Path to the input file.
    <line_index>: Index of the line to retrieve (0-based).

### Display Index File Contents

To display the contents of the index file, use the following command:

    python process_file.py <file_path>

    <file_path>: Path to the input file.