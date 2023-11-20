#!/bin/bash

# up the version of mypackage
# $1 is major, minor, or patch ; the version type to increment

# usage sh bump-version.sh minor ; sh bump-version.sh major ; sh bump-version.sh patch

pipenv run bumpversion --verbose --list $1 setup.py
git push origin --tags
git push