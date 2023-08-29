# Difference Generator

### Hexlet tests and linter status:
[![Actions Status](https://github.com/irakuruss/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/irakuruss/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3f10fbe2a4cc417ffd52/maintainability)](https://codeclimate.com/github/irakuruss/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3f10fbe2a4cc417ffd52/test_coverage)](https://codeclimate.com/github/irakuruss/python-project-50/test_coverage)
[![Python CI](https://github.com/irakuruss/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/irakuruss/python-project-50/actions/workflows/main.yml)
___
### Description
Difference Generator is a tool that determines the difference between two data structures.

Features:
 - Supported file formats: JSON, YAML.
 - Output as plain text, structured text or JSON.

Built With
- Python
- Poetry
- PyYAML
- JSON
- Pytest
- flake8
- argparse
___
### Installation
1. Clone project.
```
git clone https://github.com/irakuruss/python-project-50.git
```
```
pip install --user git+https://github.com/irakuruss/python-project-50.git
```
2. This project using Poetry, install it for next steps.
3. Go to ur local directory with project and use `make build` command for creating the package.
4. For installation use `python3 -m pip install --user dist/*.whl` command, or `make package-install`
___
### Usage
To display help information for the utility, run the following command: 
`gendiff -h`

The program takes two arguments as input - the paths to the configuration files that need to be compared: 
`gendiff first_file second_file`

The comparison result can be displayed in different formats. To specify the output format, use the option --format:
`gendiff -f FORMAT first_file second_file`
___
### Stylish format

If no format option is provided, output will be provided in stylish format.

The difference is based on how the files have changed relative to each other, the keys are rendered in alphabetical order.

The absence of a plus or minus indicates that the key is in both files, and its values coincide. In all other situations, the value of the key is either different, or the key is only in one file.
___
### Plain format

Plain format reflects the situation as if we had combined the second object with the first one.

If the new value of the property is a complex value, [complex value] is provided.
If the property is nested, then the entire path to the root is displayed, not just including the parent.
___
### JSON format

In addition to an unstructured output (as a text), often an output in a structured format, such as JSON, is needed.

JSON (JavaScript Object Notation) is a standard text format for representing structured data based on JavaScript object syntax. It is usually used to transfer data in web applications (e.g. sending some data from the server to the client so that it can be displayed on a web page or vice versa).
___
1. Calculate diff in flat files (JSON)
[![asciicast](https://asciinema.org/a/tNWxhfCoAZ5HgWi6pNJQCHQ29.svg)](https://asciinema.org/a/tNWxhfCoAZ5HgWi6pNJQCHQ29)
___
2. Calculate diff in flat files (YAML)
[![asciicast](https://asciinema.org/a/qDOp2Y2ECv107YZkTwulwLhjR.svg)](https://asciinema.org/a/qDOp2Y2ECv107YZkTwulwLhjR)
___
3. Calculate diff in recursive files (JSON)
[![asciicast](https://asciinema.org/a/ql7k0v3b9AhKx4n5ArVN0dvvD.svg)](https://asciinema.org/a/ql7k0v3b9AhKx4n5ArVN0dvvD)
___
4. Calculate diff in recursive files (YAML)
[![asciicast](https://asciinema.org/a/Spbt7D5QcxGyFYaioawqjn7xI.svg)](https://asciinema.org/a/Spbt7D5QcxGyFYaioawqjn7xI)
___
5. Examples with Plain format
[![asciicast](https://asciinema.org/a/ZjwQ02DScR4aM9aS9jIVG40j6.svg)](https://asciinema.org/a/ZjwQ02DScR4aM9aS9jIVG40j6)
___
6. Examples with JSON format:
[![asciicast](https://asciinema.org/a/yB4ONwbLWR0ZLtIuwly2qbuRL.svg)](https://asciinema.org/a/yB4ONwbLWR0ZLtIuwly2qbuRL)
