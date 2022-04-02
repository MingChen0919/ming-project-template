import os
from pathlib import Path
import re

proj_dir = os.path.dirname(Path(__file__).absolute())

for path, subdirs, files in os.walk(os.path.join(proj_dir, 'py_files')):
    for name in files:
        py_f = os.path.join(path, name)
        nb_f = re.sub('\\.py$', '.ipynb', py_f).replace('py_files', 'nb_files')
        if not os.path.exists(nb_f):
            os.remove(py_f)
            print(f'removed orphaned py file {py_f}')
