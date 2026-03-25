# 场景：实现一个命令行工具，用于复制文件或目录。
# 要求：接受源文件/目录和目标路径作为参数，并复制源文件/目录到目标路径。

import argparse
import os
import shutil

def copy_file_or_directory(src, dst):
    """
    Copy a file or directory from src to dst.
    
    If src is a file, it will be copied to dst. If dst is a directory, the file will be
    copied inside that directory with the same name. If dst is a file path, the file
    at src will be copied to dst, overwriting dst if it exists.
    
    If src is a directory, the entire directory tree will be copied to dst. If dst is a
    directory, the contents of src will be copied inside dst. If dst is a file path, an
    error will be raised because you cannot copy a directory to a file path.
    
    :param src: Source file or directory path
    :param dst: Destination file or directory path
    """
    if os.path.isdir(src):
        # If src is a directory, copy the entire directory tree
        if os.path.exists(dst) and not os.path.isdir(dst):
            raise ValueError(f"Destination {dst} is a file, but source {src} is a directory. Cannot copy directory to file.")
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        # If src is a file, copy the file to dst
        if os.path.isdir(dst):
            # If dst is a directory, append the file name to the destination path
            dst = os.path.join(dst, os.path.basename(src))
        shutil.copy2(src, dst)

def main():
    parser = argparse.ArgumentParser(description="Copy a file or directory to a destination.")
    parser.add_argument("src", help="Source file or directory to copy")
    parser.add_argument("dst", help="Destination file or directory path")
    args = parser.parse_args()
    
    try:
        copy_file_or_directory(args.src, args.dst)
        print(f"Successfully copied {args.src} to {args.dst}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()

#如果目标是一个目录，文件将被复制到该目录内。如果目标是一个文件路径，源文件将被复制到目标文件路径，覆盖目标文件（如果存在）。
