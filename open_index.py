import struct
import sys
import os

def display_index_file(index_file_path):
    """Display the contents of the index file."""
    try:
        with open(index_file_path, "rb") as index_file:
            index_size = os.path.getsize(index_file_path)
            num_offsets = index_size // 8  # Each offset is 8 bytes
            print(f"Index file contains {num_offsets} offsets:")
            for i in range(num_offsets):
                offset_data = index_file.read(8)
                offset = struct.unpack('Q', offset_data)[0]
                print(f"Offset {i}: {offset}")
    except Exception as e:
        print(f"Error reading index file: {e}")
        
def main():
    """Main function to handle command line arguments and execution."""
    if len(sys.argv) != 2:
        print("Usage: python display_index_file.py <index_file_path>")
        return

    index_file_path = sys.argv[1]
    display_index_file(index_file_path)
    
if __name__ == "__main__":
    main()