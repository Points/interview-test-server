import markdown
import os

ROOT_DIR = os.path.dirname(__file__)

with open(os.path.join(ROOT_DIR, 'README.md'), 'r') as f:
    text = f.read()
    html = markdown.markdown(text, extensions=['tables', 'fenced_code'])


dest_file = os.path.join(ROOT_DIR, 'templates', 'generated.html')

with open(dest_file, 'w') as f:
    f.write(html)
