from subprocess import run
import os
from os.path import join
from typing import List, Dict
import shutil
from yaml import dump, load
from docs_generator.Document import Document, Folder
from docs_generator.config import *
from docs_generator.utils import walk_folders, generate_markdown, generate_config

if __name__ == '__main__':
    fs = walk_folders(notebook_folder)
    # generate_markdown(fs)
    config = generate_config(fs)
    o = dump(config, indent=4)
    with open(config_filename, 'w') as f:
        f.write(o)
    # p = {'A': {'B': ['Merge sort', 'Insertion sort', 'Selection sort']}}
    # c = create_object(p, ['a', 'b', 'c'], [Document('a/b/c/d.txt')])
    # print(c)
