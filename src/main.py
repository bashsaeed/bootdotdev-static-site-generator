import os
import sys
from generate_page import generate_pages_recursive
from copy_directory import copy_directory

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    args: list[str] = sys.argv
    basepath = args[1] if len(args) > 1 else default_basepath
    copy_directory(dir_path_static, dir_path_public)
    generate_pages_recursive(
        dir_path_content, template_path, dir_path_public, basepath
    )


if __name__ == "__main__":
    main()
