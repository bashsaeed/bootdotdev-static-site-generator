import os
import sys
from generate_page import generate_pages_recursive
from copy_directory import copy_directory

dir_path_static = "static"
dir_path_public = "docs"
dir_path_content = "content"
template_path = "template.html"


def main():
    args: list[str] = sys.argv
    basepath = args[1] if len(args) > 1 else "./"
    copy_directory(dir_path_static, dir_path_public)
    generate_pages_recursive(
        os.path.join(basepath, dir_path_content),
        os.path.join(basepath, template_path),
        os.path.join(basepath, dir_path_public),
    )


if __name__ == "__main__":
    main()
