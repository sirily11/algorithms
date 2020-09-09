from subprocess import run
import os
from os.path import join
from typing import List, Dict
import shutil
from yaml import dump, load
from docs_generator.Document import Document, Folder

# site_name: My Docs
# theme:
#   name: material
#
# nav:
#   - 'Sort':
#       - 'Merge Sort': 'merge_sort.md'
#
# markdown_extensions:
#   - pymdownx.arithmatex:
#       generic: true
#   - pymdownx.highlight:
#       use_pygments: true
#   - codehilite
#   - toc:
#       permalink: true
#
# extra_javascript:
#   - javascripts/config.js
#   - "https://polyfill.io/v3/polyfill.min.js?features=es6"
#   - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

config_filename = 'mkdocs.yml'
notebook_folder = 'notebooks'
output_dir_name = 'docs'
ignore_folder = '.ipynb_checkpoints'


# run(['jupyter', 'nbconvert', "--output-dir='./docs'", "--to", "markdown", "notebooks/sort/merge_sort.ipynb"])


def walk_folders(folder_name: str) -> List[Folder]:
    folders = []
    for dirName, subdirList, fileList in os.walk(folder_name):
        if ignore_folder not in dirName:
            if not fileList:
                continue
            new_folder_name = dirName.replace(f'{folder_name}/', '')
            folder = Folder(new_folder_name)
            new_file_list = [Document(join(dirName, f)) for f in fileList if '.ipynb' in f]
            folder.add_files(new_file_list)
            folders.append(folder)
    return folders


def generate_markdown(folders: List[Folder]):
    if os.path.exists(output_dir_name):
        os.remove(output_dir_name)
    for folder in folders:
        output_dir = os.path.join(output_dir_name, folder.name)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for file in folder.files:
            run(['jupyter', 'nbconvert', f"--output-dir='{output_dir_name}'", "--to", "markdown", file.path,
                 f"--output",
                 f"{file.get_output_name(notebook_folder)}"])
            # print(file.get_output_name(notebook_folder))


def generate_config(folders: List[Folder]):
    configuration = {
        "site_name": "Algorithm",
        "nav": [],
        "theme": {"name": "material"},
        "extra_javascript": [
            "javascripts/config.js",
            "https://polyfill.io/v3/polyfill.min.js?features=es6",
            "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
        ],
        "markdown_extensions": [
            {"pymdownx.arithmatex": {
                "generic": True
            },
            },
            {
                "pymdownx.highlight": {
                    "use_pygments": True
                }
            },

            "codehilite",
            {
                'toc': {
                    'permalink': True
                }
            }
        ]
    }
    navs = {}
    for folder in folders:
        name_list = folder.get_list_folder_names()
        navs = create_object(navs, name_list, folder.files)
    configuration['nav'] = navs
    return configuration


def create_object(prev_nav: Dict, name_list: List[str], files: List[Document]):
    name = name_list[0].capitalize()
    if len(name_list) == 1:
        new_files = [f.get_name() for f in files]
        if name in prev_nav:
            prev_content = prev_nav[name]
            prev_content += new_files
            prev_nav[name] = prev_content
            return prev_nav
        else:
            return {
                name: new_files
            }
    else:
        if name in prev_nav:
            prev_content = prev_nav[name]
            if isinstance(prev_content, list):
                f = create_object(prev_nav[name], name_list[1:], files)
                prev_content += [f]
            else:
                prev_content = create_object(prev_nav[name], name_list[1:], files)
            prev_nav[name] = prev_content
            return prev_nav
        else:
            return {
                name: create_object(prev_nav, name_list[1:], files)
            }


if __name__ == '__main__':
    fs = walk_folders(notebook_folder)
    generate_markdown(fs)
    config = generate_config(fs)
    o = dump(config, indent=4)
    with open(config_filename, 'w') as f:
        f.write(o)
    # p = {'A': {'B': ['Merge sort', 'Insertion sort', 'Selection sort']}}
    # c = create_object(p, ['a', 'b', 'c'], [Document('a/b/c/d.txt')])
    # print(c)
