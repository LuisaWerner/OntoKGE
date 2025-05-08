import sys


def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                parts = line.strip().split('\t')
                if len(parts) == 3:
                    parts[1] = parts[1].lstrip('_')  # Remove leading underscore
                    file.write('\t'.join(parts) + '\n')
                else:
                    file.write(line)  # Write unchanged if format is unexpected

        print(f"Processed file: {filename}")
    except Exception as e:
        print(f"Error processing file: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        process_file(sys.argv[1])
