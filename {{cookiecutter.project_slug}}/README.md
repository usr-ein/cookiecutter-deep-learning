# {{cookiecutter.project_name}}

{{cookiecutter.project_desc}}

## Getting started

To run this repository, you will need to install [Poetry](https://github.com/python-poetry/poetry), a popular dependencies 
and virtual environments' manager for Python.

Once you have that, run the following commands:
```sh
git clone git@github.com:{{cookiecutter.org_github_name}}/{{cookiecutter.project_slug}}.git {{cookiecutter.project_slug}}
cd {{cookiecutter.project_slug}}
poetry install
poetry run python3 {{cookiecutter.project_slug}}/eval/eval.py --help
```

## Usage
```
usage: eval.py [-h] [-o OUTPUT] [-i INT_PARAM]
               [--float_param_optional FLOAT_PARAM_OPTIONAL] [-v]
               input

{{cookiecutter.project_desc}}

positional arguments:
  input                 Input dataset

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Where to write the output
  -i INT_PARAM, --int_param INT_PARAM
                        Cool int param.
  --float_param_optional FLOAT_PARAM_OPTIONAL
                        Cool optional float param.
  -v, --verbose         Displays helpful information along.

```
