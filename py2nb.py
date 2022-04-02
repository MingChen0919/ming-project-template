#!/opt/miniconda3/bin/python
"""Create a notebook containing code from a script.

This script is a modified version of https://github.com/williamjameshandley/py2nb. It creates the corresponding .ipynb
file within the nb_files directory instead of the same folder of the .py file.
Run as:  python to_noteebook.py my_script.py
"""
import argparse
import os
from pathlib import Path
import re
import nbformat.v4

ACCEPTED_CHARS = ['#-', '# -']  # separating line for readability
MARKDOWN_CHARS = ['#|', '# |']
ACCEPTED_CHARS.extend(MARKDOWN_CHARS)


def new_cell(nb, cell, markdown=False):
    """ Create a new cell

    Parameters
    ----------
    nb: nbformat.notebooknode.NotebookNode
        Notebook to write to, as produced by nbformat.v4.new_notebook()

    cell: str
        String to write to the cell

    markdown: boolean, optional, (default False)
        Whether to create a markdown cell, or a code cell
    """
    cell = cell.rstrip().lstrip()
    if cell:
        if markdown:
            cell = nbformat.v4.new_markdown_cell(cell)
        else:
            cell = nbformat.v4.new_code_cell(cell)
        nb.cells.append(cell)
    return ''


def str_starts_with(string, options):
    for opt in options:
        if string.startswith(opt):
            return True


def convert(py_file_location):
    """ Convert the python script to jupyter notebook"""
    with open(py_file_location) as f:
        markdown_cell = ''
        code_cell = ''
        nb = nbformat.v4.new_notebook()  # create a new empty notebook
        for line in f:
            if str_starts_with(line, ACCEPTED_CHARS):
                code_cell = new_cell(nb, code_cell)
                if str_starts_with(line, MARKDOWN_CHARS):
                    # find the first occurrence of |
                    # and add the rest of the line to the markdown cell
                    markdown_cell += line[line.index('|') + 1:]
                else:
                    markdown_cell = new_cell(nb, markdown_cell, markdown=True)
            else:
                markdown_cell = new_cell(nb, markdown_cell, markdown=True)
                line = re.sub('#.*>', '', line)  # lines start with `#>` or `# >` will be treated as a code cell
                line = line.lstrip()
                code_cell += line

        # process the last markdown or code cell
        markdown_cell = new_cell(nb, markdown_cell, markdown=True)
        code_cell = new_cell(nb, code_cell)

        notebook_name = os.path.splitext(py_file_location)[0] + '.ipynb'
        notebook_name = notebook_name.replace('py_files', 'nb_files')
        dir_name = os.path.dirname(os.path.abspath(notebook_name))
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        nbformat.write(nb, notebook_name)
        print(f'converted {py_file_location} to a notebook')


def parse_args():
    """Argument parsing for py2nb"""
    description = "Convert a python script to a jupyter notebook"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "py_file_location",
        help="Path to a .py file or directory that has .py files")
    return parser.parse_args()


def main():
    args = parse_args()
    if os.path.isfile(args.py_file_location):
        if args.py_file_location.endswith('.py'):
            convert(args.py_file_location)
    elif os.path.isdir(args.py_file_location):
        for path, subdirs, files in os.walk(args.py_file_location):
            for name in files:
                f = os.path.join(path, name)
                if f.endswith('.py'):
                    convert(f)


if __name__ == '__main__':
    main()
