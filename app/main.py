import sys
import os
import zlib

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    command = sys.argv[1]
    
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    if command == "cat-file":
        flag = sys.argv[2]
        hash_name = sys.argv[3]
        if flag == "-p":
            with open(f".git/objects/{hash_name[:2]}/{hash_name[2:]}", "rb") as f:
                blob = f.read()
                decompressed_content = zlib.decompress(blob)
                length = decompressed_content[6:]
                print(decompressed_content[decompressed_content.find(b'\x00')+1:].decode('utf8'), end="")
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
