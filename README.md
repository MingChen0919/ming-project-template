# [Ming Project Template](https://mingchen0919.github.io/ming-project-template/)

[Py Files](https://mingchen0919.github.io/ming-project-template/py_files.html)

# Set up project directory

All the documents/tutorials are written as a `.py` file in a python IDE and then converted to `.ipynb` using the python
package [py2nb](https://github.com/williamjameshandley/py2nb). The files will then be displayed as a clickable
tree in html format that can be display on github directly. The project directory is setup by using this
template https://github.com/MingChen0919/ming-project-template.

We clone the project template repo and rename the repo using the actual project name.

```
!git clone git@github.com:MingChen0919/ming-project-template.git my_project_name
```

The next step is to edit the `.Rmd` files so that it can recognize the right project repo. We need to replace all
`ming-project-template`s with the actual project name. Here we search and replace `ming-project-template` with
 `my_project_name`. I also edit the text in the .Rmd to add descriptions for this specific project.

We then turn on the **GitHub Pages** feature to host the HTML pages. Go to
https://github.com/MingChen0919/ming-project-template/settings/pages and select `Branch: main` and `/root` for
the **source** section.

Whenever you finish writing a `.py` file, you can convert it to a `.ipynb` with the modified [py2nb.py](./py2nb.py) 
script. It will automatically place the `.ipybn` file within the **nb_files** directory.

```shell script
./py2nb.py my_script.py
```

You can also convert all `.py` files within a folder and its sub-folders

```shell script
./py2nb.py py_files
```


Whenever you have **new** `.ipynb` file(s) being generated, you will need to run the `.Rmd` files in R to
generate (update) HTML pages. If you just update the `.ipynb` files, you don't have to run the `.Rmd` files.

To clean up orphaned `.ipynb` files:

```shell script
python clean_up.py
```