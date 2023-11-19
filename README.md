# Steps to build the package
- pip install setuptools wheel
## Create the whl file
- python setup.py sdist bdist_wheel
- After running the above command, you should find your .whl file in the dist/ directory.
  - the file is, dist/mypackage-0.1.0-py3-none-any.whl
## Using the wheel file
- pip install dist/mypackage-0.1.0-py3-none-any.whl, now this package is ready for use.
  - running pip list will show the pkg_example_project, see
    ```
    Package             Version
    ------------------- -------
    bumpversion         0.5.3
    pip                 23.3.1
    mypackage           0.1.0 *
    setuptools          68.2.2
    wheel               0.41.2
    ```
## use the above installed package
```python
from mypackage.mymodule import hello_world
print(hello_world())
```
## run pytest
- pip install pytest
- pytest -vv tests/

## requirements file
- pip freeze > requirements.txt

## how to manage package version
- pip install bumpversion
- You need to configure bumpversion to know where to find and how to update the version number.
This can be done either in a .bumpversion.cfg file, directly in setup.cfg under a [bumpversion] section, 
or in pyproject.toml for newer Python projects.
- when the package is create version number line is added to both setup.py and my_package/__init__.py
- Here's an example for setup.cfg:
```asciidoc
[bumpversion]
current_version = 0.1.0
commit = True
tag = True
tag_name = {new_version}

[bumpversion:file:setup.py]
search = version='{current_version}'
replace = version='{new_version}'

[bumpversion:file:my_package/__init__.py]
search = __version__ = '{current_version}'
replace = __version__ = '{new_version}'

```
- Above configuration will:
  - Define the current version of the project.
  - Automatically commit the version bump to Git and tag the commit.
  - Update the version number in both setup.py and __init__.py of your package.
## Bumping Version 
- Whenever you want to update the version, you can now run bumpversion with the specific part of the version you want to update (major, minor, or patch):
```shell
bumpversion patch  # for a patch version bump, e.g., 0.1.0 to 0.1.1

# Above command will
# Update the version in setup.py and __init__.py.
# Commit these changes to your Git repository (if commit is set to True).
# Optionally, create a Git tag (if tag is set to True).
```

## Adding another module, utils to the package
- pip install psycopg2-binary


## List all the modules inside the package
```python
import mypackage
dir(mypackage)
```