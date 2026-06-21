# calc-utils

A small Python calculator and utility library, built as a hands-on learning
project covering **version control (Git/GitHub)**, **continuous integration
(GitHub Actions)**, and **quality assurance (unit tests + linting)**.

## Features

- Basic arithmetic: `add`, `subtract`, `multiply`, `divide`, `power`
- String utilities: `is_palindrome`, `reverse_string`, `word_count`

## Installation

```bash
git clone https://github.com/<your-username>/calc-utils.git
cd calc-utils
pip install -r requirements.txt
```

## Usage

```python
from calc_utils import add, divide
from calc_utils.string_utils import is_palindrome

print(add(2, 3))          # 5
print(divide(10, 2))      # 5.0
print(is_palindrome("Racecar"))  # True
```

## Running tests

```bash
pytest
```

## Linting

```bash
flake8 calc_utils tests
```

## CI

Every push and pull request triggers a GitHub Actions workflow
(`.github/workflows/ci.yml`) that installs dependencies, lints the code with
`flake8`, and runs the test suite with `pytest`.

## Project docs

- [QA Report](QA_REPORT.md)
- [Reflection](REFLECTION.md)
