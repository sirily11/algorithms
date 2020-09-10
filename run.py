from yaml import dump, load
from docs_generator.config import *
from docs_generator.utils import walk_folders, generate_markdown, generate_config

if __name__ == '__main__':
    fs = walk_folders(notebook_folder)
    generate_markdown(fs)
    config = generate_config(fs)
    o = dump(config, indent=4)
    with open(config_filename, 'w') as f:
        f.write(o)

    with open('index.md', 'r') as f:
        content = f.read()
        with open('docs/index.md', 'w') as f1:
            f1.write(content)
