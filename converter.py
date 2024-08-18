import sys
import subprocess
import os

def convert_to_opus(input_file):
    base = os.path.splitext(input_file)[0]
    output_file = f"{base}.opus"

    command = ['ffmpeg', '-i', input_file, '-c:a', 'libopus', output_file]

    subprocess.run(command)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        convert_to_opus(input_file)
    else:
        print("Please drag and drop a file onto this script.")

