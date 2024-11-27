import os
import sys
import struct

def create_index(file_path):
    """Create an index file with accurate line offsets."""
    index_file_path = f"{file_path}.idx"

    try:
        with open(file_path, "r", newline="") as file:
            offset = 0
            with open(index_file_path, "wb") as index_file:
                for line in file:
                    index_file.write(struct.pack('Q', offset))  # Write offset as unsigned long long (8 bytes)
                    offset += len(line.encode("utf-8"))  # Use the actual byte length to update the offset
        print(f"Writing index to {index_file_path}... done.")
    except Exception as e:
        print(f"Error creating index file: {e}")

def get_offset(index_file_path, line_index):
    """Retrieve the byte offset for the specified line index."""
    try:
        with open(index_file_path, "rb") as index_file:
            index_file.seek(line_index * 8)  # Each offset is 8 bytes
            offset_data = index_file.read(8)
            if not offset_data:
                raise ValueError("Invalid line index")
            return struct.unpack('Q', offset_data)[0]
    except Exception as e:
        print(f"Error reading index file: {e}")
        raise

def get_line(file_path, line_index):
    """Retrieve the specific line from the file using the index."""
    index_file_path = f"{file_path}.idx"

    try:
        # Get the byte offset for the specified line index
        start_offset = get_offset(index_file_path, line_index)

        # Read the file and seek to the line's start offset
        with open(file_path, "r") as file:
            file.seek(start_offset)
            # Read the line starting from the offset
            line = file.readline()
            print(line, end='')  # Use end='' to avoid adding extra newline
    except FileNotFoundError:
        print(f"Error: Index file {index_file_path} not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to handle command line arguments and execution."""
    if len(sys.argv) != 3:
        print("Usage: python process_file.py <file_path> <line_index>")
        return

    file_path = sys.argv[1]
    try:
        line_index = int(sys.argv[2])
    except ValueError:
        print("Error: Line index must be an integer.")
        return

    # Check if the index file exists
    index_file_path = f"{file_path}.idx"
    if not os.path.exists(index_file_path) or os.path.getsize(index_file_path) == 0:
        # If the index file doesn't exist or is empty, create it
        create_index(file_path)

    # Retrieve the requested line
    get_line(file_path, line_index)

if __name__ == "__main__":
    main()