import os

from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str
) -> None:
    for root, _, files in os.walk(dir_path_content):
        for filename in files:
            if not filename.endswith(".md"):
                continue

            # Full path to the input markdown file
            from_path = os.path.join(root, filename)

            # Relative path from the content root
            relative_path = os.path.relpath(from_path, dir_path_content)

            # Change extension from .md to .html
            relative_html_path = os.path.splitext(relative_path)[0] + ".html"

            # Full path to the destination HTML file
            dest_path = os.path.join(dest_dir_path, relative_html_path)

            # Generate the page using your earlier function
            generate_page(from_path, template_path, dest_path, basepath)


def generate_page(
    from_path: str, template_path: str, dest_path: str, basepath: str
) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Read template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Replace placeholders
    final_html = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", html_content)
        .replace('href="/', 'href="' + basepath)
        .replace('src="/', 'src="' + basepath)
    )

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write final HTML
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)


def extract_title(markdown: str) -> str:
    lines = markdown.splitlines()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("##"):
            return stripped[2:].strip()
    raise ValueError("No H1 header found in markdown.")
