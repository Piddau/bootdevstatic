import os
import shutil
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in markdown")

def move_static_files(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    os.mkdir(dest_dir)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} to {dest_path}")
        else:
            move_static_files(src_path, dest_path)

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        markdown_content = f.read()
        with open(template_path, 'r') as tf:
            template_content = tf.read()
            
            html_content = markdown_to_html_node(markdown_content).to_html()
            title = extract_title(markdown_content)
            full_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
            full_page = full_page.replace('href="/', f'href="{basepath}')
            full_page = full_page.replace('src="/', f'src="{basepath}')
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            with open(dest_path, 'w') as df:
                df.write(full_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    entries = os.listdir(dir_path_content)
    
    for entry in entries:
        full_path = os.path.join(dir_path_content, entry)
        
        if os.path.isfile(full_path) and entry.endswith('.md'):
            # Generate HTML for markdown files
            rel_file = os.path.splitext(entry)[0] + '.html'
            dest_path = os.path.join(dest_dir_path, rel_file)
            generate_page(full_path, template_path, dest_path, basepath)
        
        elif os.path.isdir(full_path):
            # Recursively process subdirectories
            dest_subdir = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(full_path, template_path, dest_subdir, basepath)

# Create a generate_pages_recursive(dir_path_content, template_path, dest_dir_path) function. It should:
# Crawl every entry in the content directory
# For each markdown file found, generate a new .html file using the same template.html. 
# The generated pages should be written to the public directory in the same directory structure.
# Change your main function to use generate_pages_recursive instead of generate_page. 
# You should generate a page for every markdown file in the content directory and write the results to the 
# public directory.
# Run the new program and ensure that both pages on the site are generated correctly and you can navigate between them.