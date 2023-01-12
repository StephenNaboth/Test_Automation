# Test Automation
## Introduction to pytest
This repository contains some code for *Introduction to [pytest](https://pytest.org)*.

## Python Setup

`python 3`

## Python Packages needed to install

* `pytest`
* `pytest-cov`
* `pytest-html`
* `pytest-xdist`
* `requests`

These packages are *not* part of Python's standard library.
They must be installed separately using `pip`, the standard Python package installer.

To install each package, enter `pip install <package-name>` at the command line.
For example: `pip install pytest`.
If you already have a package installed but need to upgrade its version,
run `pip install --upgrade <package-name>`.

Please note that if you need to use the `python3` command to run Python,
then you might also need to use the `pip3` command in lieu of `pip`.

### Virtual Environments

Running `pip install` will install the pytest package globally for the whole system.
Installing Python packages globally is okay for this course,
but it typically isn't a best practice in the "read world."
Instead, each project should manage its own dependencies locally using a virtual environment.
Virtual environments let projects avoid unnecessary dependencies and version mismatches.

If you would like to learn virtual environments on your own, then RealPython's article
[Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
is an excellent place to start.


## Running Tests

To run the example tests from the command line, run `python -m pytest` from the project root directory.
This command will discover and run all tests in the project.

You can also run tests using the shorter `pytest` command.
However, I recommend always using the lengthier `python -m pytest` command.
The lengthier command automatically adds the current directory to `sys.path`
so that all modules in the project can be discovered.

The pytest command has several command line options.
Course material will cover many of them.
Check out the [Usage and Invocations](https://docs.pytest.org/en/stable/usage.html) page
for complete documentation.







