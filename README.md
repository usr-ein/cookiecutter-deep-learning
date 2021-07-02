# Cookiecutter Deep Learning

This repo contains a [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) templates aimed at deep learning and AI research. 

It can come in handy for projects that involve a lot of experimentation, source material, training models, evaluating models, documenting everything etc.

## Iteration time
Unlike many Python cookiecutter templates aimed at software engineering, this template doesn't have any:
 - Unit test hook with pytest
 - CI/CD with travis or so
 - PyPI deployment scripts
 - Sphinx documentation
 
This is because, when researching, the need for all that only arise much later. At the beginning it would be detrimental to implement all those mechanisms because "iterations" happen so fast. It would create too much friction which would make switching to a new paper, a new implementation, a new architecture, or a new dataset way harder than it needs to be.

## Usage
### 1. Install Cookie Cutter

```sh
pip3 install cookiecutter
```

### 2. Generate your project

Now it’s time to generate your project's python package.
Use cookiecutter, pointing it at the cookiecutter-deep-learning repo:
```sh
cookiecutter https://github.com/sam1902/cookiecutter-deep-learning.git
```
You’ll be asked to enter a bunch of values to set the package up. If you don’t know what to enter, stick with the defaults.

### 3. Create a GitHub Repo

Go to your GitHub account and create a new repo named mypackage, where mypackage matches the `[project_slug]` from your answers to running cookiecutter. This is so that the rest of the project generation can work seamlessly.

You will find one folder named after the `[project_slug]`. Move into this folder, and then setup git to use your GitHub repo and upload the code:

```sh
cd project_slug
git init .
git add .
git commit -m "Initial skeleton."
git remote add origin git@github.com:myusername/project_slug.git
git push -u origin master
```

Where `myusername` and `project_slug` are adjusted for your username and project slug.

You’ll need a ssh key to push the repo. You can [Generate](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) a key or [Add](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) an existing one.

### 4. Setup `poetry`

To handle dependencies, I recommend installing and using [`poetry`](https://python-poetry.org/docs/). Once that is done, you can initialise the environment like so:
```sh
poetry install
```

To add new dependencies, you can either add release dependencies:
```sh
poetry add numpy
```
or you can add *dev only* dependencies:
```sh
poetry add -D pytest
```
