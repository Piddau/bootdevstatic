import sys
from file_handling import move_static_files, generate_pages_recursive
from textnode import TextNode

basepath = "/"

def main():
    move_static_files("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    main()
    
# Right now our site always assumes that / is the root path of the site (e.g. http://localhost:8888/. Make it configurable by:
# In main.py use the sys.argv to grab the first CLI argument to the program. Save it as the basepath. If one isn't provided, default to /.
# Pass the basepath to the generate_pages_recursive and generate_page functions.
# In generate_page, after you replace the {{ Title }} and {{ Content }}, replace any instances of:
# href="/ with href="{basepath}
# src="/ with src="{basepath}