import os
import shutil


def copy_directory(src="static", dst="public"):

    # Step 0: Check if source directory exists
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source directory does not exist at: {src}")

    # Step 1: Delete the destination directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Deleted existing destination: {dst}")

    # Step 2: Recreate the destination directory
    os.mkdir(dst)
    print(f"Created destination: {dst}")

    # Step 3: Recursively copy contents
    def recursive_copy(src_dir, dst_dir):
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dst_path = os.path.join(dst_dir, item)

            if os.path.isfile(src_path):
                shutil.copy(src_path, dst_path)
                print(f"Copied file: {src_path} → {dst_path}")
            else:
                os.mkdir(dst_path)
                print(f"Created directory: {dst_path}")
                recursive_copy(src_path, dst_path)

    recursive_copy(src, dst)


if __name__ == "__main__":
    copy_directory("static", "public")
