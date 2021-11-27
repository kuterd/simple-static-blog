from datetime import date
from jinja2 import Environment, FileSystemLoader
from os import path
import markdown
import copy

RENDERED_FOLDER = "result"
ENTRIES_FOLDER = "entries"

class BlogEntry:
    def __init__(self, title, description, content, date):
        self.title = title
        self.description = description

        content_file = open(path.join(ENTRIES_FOLDER, content))
        self.content = markdown.markdown(content_file.read(), extensions=['codehilite','fenced_code'])
        self.date = date.strftime("%d-%m-%Y")
        self.url = title.lower().replace(' ', '-') + ".html"

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

def render_page(file_name, tmp_name, params):
    template = env.get_template(tmp_name)
    result = template.render(**params)
    rfile = open(path.join(RENDERED_FOLDER, file_name), "w")
    rfile.write(result)

def render_all(general, entries):
    index_info = copy.copy(general)
    index_info["entries"] = entries

    render_page("index.html", "index.html", index_info) 

    for entry in entries:
        entry_info = copy.copy(general)
        entry_info["entry"] = entry
        render_page(entry.url, "blog_entry.html", entry_info)

entries = [
    BlogEntry("Making a very simple static blog generator", "This is a description", "test.md", date.today()),
    BlogEntry("A entry without description", "", "test.md", date.today()),
    BlogEntry("Lorem ipsum", "Very descriptive", "lorem-ipsum.md", date.today()),
    BlogEntry("Code highlight test", "Testing if we can highlight code in markdown", "code_test.md", date.today())
]

render_all({"author": "Replace Me"}, entries)
