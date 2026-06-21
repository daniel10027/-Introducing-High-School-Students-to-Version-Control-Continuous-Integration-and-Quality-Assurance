# QA Report — calc-utils

## 1. Unit Tests

13 unit tests were written using `pytest`, covering every public function in
the library. All tests currently pass.

| Module | Test file | Functions covered | # Tests |
|---|---|---|---|
| `calc_utils/operations.py` | `tests/test_operations.py` | `add`, `subtract`, `multiply`, `divide`, `power`, `modulo` | 8 |
| `calc_utils/string_utils.py` | `tests/test_string_utils.py` | `is_palindrome`, `reverse_string`, `word_count`, `shout` | 5 |

**Edge cases covered:**
- Division by zero (`divide`) → raises `ValueError`
- Modulo by zero (`modulo`) → raises `ValueError`
- Negative numbers in arithmetic operations
- Empty strings in `reverse_string` and `word_count`
- Mixed-case and punctuation in `is_palindrome` (e.g. "Was it a car or a cat I saw?")

**Result of last full run:**
```
13 passed in 0.03s
```

## 2. Linter Findings (flake8)

`flake8` was run against `calc_utils/` and `tests/` (max line length 100).

| File | Line | Code | Issue | Resolution |
|---|---|---|---|---|
| `calc_utils/string_utils.py` | 22 | E231 | Missing whitespace after `:` in function signature | Added space after colon in type hint |
| `calc_utils/string_utils.py` | 22 | E225 | Missing whitespace around `->` operator | Added spaces around return-type arrow |
| `calc_utils/string_utils.py` | 23 | F841 | Local variable `unused_var` assigned but never used | Removed the unused variable |

After fixes, `flake8` reports **zero issues** on the codebase. This check is
also enforced automatically in CI on every push and pull request, so the
codebase cannot regress on style without the build failing.

```
$ flake8 calc_utils tests --max-line-length=100
(no output — clean)
```

## 3. Code Review Summary

Two simulated pull requests were used to practice the GitHub review workflow:

### PR: "Add string utilities"
- **Branch:** `feature/string-utils` → `master`
- **Changes:** Added `is_palindrome`, `reverse_string`, `word_count`, `shout`
  with accompanying tests.
- **Conflict encountered:** Merging this branch coincided with an unrelated
  docstring wording change on `master`. Git's auto-merge resolved it cleanly
  since the changes touched different lines; no manual conflict resolution
  was needed here.

### PR: "Add modulo operation" (PR review with requested changes)
- **Branch:** `feature/modulo-operation` → `master`
- **Initial submission:** `modulo(a, b)` with no type hints, no docstring,
  and no protection against division by zero.
- **Reviewer feedback (simulated):**
  1. "Please add type hints and a docstring, consistent with the other
     functions in `operations.py`."
  2. "This will throw an unhandled `ZeroDivisionError` if `b == 0`. Other
     functions in this module raise a clear `ValueError` instead — please
     match that pattern."
  3. "No test coverage for this function — please add unit tests, including
     the zero-divisor case."
- **Author response:** All three points addressed in a follow-up commit:
  type hints and docstring added, `ValueError` guard added for `b == 0`,
  and two new tests added (`test_modulo`, `test_modulo_by_zero_raises`).
- **Outcome:** Approved and merged via `--no-ff` merge commit, preserving
  the review history on the branch.

### Real merge conflict (version bump)
A genuine merge conflict was also created and resolved as part of this
exercise: two branches (`feature/bump-version-a`, `feature/bump-version-b`)
each modified the same `__version__` line in `calc_utils/__init__.py`.
Merging the second branch into `master` produced a real `CONFLICT (content)`
error. The conflict markers were inspected manually, the higher version
number (`0.2.0`) was kept as the correct resolution, and the test suite was
re-run before committing the merge to confirm nothing broke.

## 4. CI Enforcement

All of the above is enforced automatically by `.github/workflows/ci.yml` on
every `push` and `pull_request` to `master`/`main`:
1. Checks out the code
2. Installs dependencies from `requirements.txt`
3. Runs `flake8` — **build fails if any lint issue is found**
4. Runs `pytest` — **build fails if any test fails**
5. Repeats across Python 3.10, 3.11, and 3.12 (test matrix)

GitHub automatically shows pass/fail status checks on every commit and pull
request, and notifies (via email/GitHub notifications) the people who
triggered a run if a build fails — no additional notification setup was
required beyond enabling the workflow.
