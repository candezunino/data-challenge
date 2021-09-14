# Data Challenge

## Content Index
  * [Prepare Environment](#prepare-environment)
  * [IDEs Configuration](#ides-configuration)
  * [Run Tests](#run-tests)

## Prepare Environment
The following section will give you the steps to configure an environment you need to create new data challenge or run the tests locally.

1. Clone the repository `git clone git@gitlab.com:factory14/data-team/data-challenge.git`.
2. Create a Python virtual environment `mkvirtualenv --python=/usr/local/opt/python@3.7/bin/python3.7 <virtual-env-name>`.
3. In order to contribute, install the required development packages `pip install -r requirements-dev.txt`.
4. Install the required runtime packages `pip install -r requirements.txt`.

### IDEs Configuration
IntelliJ / Pycharm should import this project without issues. You may want to configure a couple of things though:
- Set the project's Python interpreter pointing to `<virtual-env-name>` virtual env:
    - File -> Project Structure -> SDKs -> Add Python SDK -> Virtualenv environment -> <choose the existing one under `~/.virtualenvs/<virtual-env-name>/bin/python` dir>
- Set the project's testing framework:
    - Preferences -> Tools -> Python integrated tools -> Testing -> Default test runner -> Choose `pytest`

### Run Tests

```sh
$ pytest ./test
```
