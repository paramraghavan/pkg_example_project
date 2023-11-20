import os
from setuptools import setup, find_packages

path = os.path.dirname(os.path.realpath(__file__))
requirement_path = os.path.join(path, "requirements.txt")

if os.path.isfile(requirement_path):
    with open(requirement_path) as f_h:
        install_requires = f_h.read().splitlines()

setup(
    name='mypackage',
    version='0.1.2',
    packages=find_packages(where="src"), # packages=["src"],
    package_dir={"": "src"},
    # install_requires=[
    #     # List your project dependencies here
    #     # e.g., 'requests >= 2.25.1'
    # ],
    python_requires='>=3.9',
    url='https://github.com/yourusername/example_project',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
)
