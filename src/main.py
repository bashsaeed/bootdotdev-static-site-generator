import os
from generate_page import generate_page
from copy_directory import copy_directory

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    copy_directory(dir_path_static, dir_path_public)
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )


if __name__ == "__main__":
    main()
