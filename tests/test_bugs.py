"""Automated checks for Activity 4: Finding Bugs.

Each check runs one program in `src/` on its own, the same way
`uv run python src/logic_1.py` does, and reads the labelled line it prints.
A line is matched loosely: any amount of whitespace, any letter case, and the
colon is optional.

Every check runs its program twice: once as written, and once with the first
value in the file changed (`rounds = 3` becomes `rounds = 5`). A fix therefore
has to work for more than the one number in the file, and that first line has
to stay in place.

When a check fails, the assertion message names the file, says whether it
stopped with an error, never finished, or printed the wrong value, and quotes
the last line of the error.
"""

import re
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"

# How long one run may take. Every program here finishes almost at once, so a
# run that takes this long has a loop that never ends.
SECONDS = 2


def run(name, tmp_path, change=None):
    """Run src/<name>.py and return what it printed.

    `change` is (variable, value): the first line that assigns `variable` is
    replaced with `variable = value` in a copy of the file, and the copy runs.
    """
    path = SRC / f"{name}.py"
    if change is not None:
        variable, value = change
        source = path.read_text(encoding="utf-8")
        pattern = rf"^{re.escape(variable)}\s*=.*$"
        if not re.search(pattern, source, re.MULTILINE):
            raise AssertionError(
                f"src/{name}.py has no line starting `{variable} =`: keep that line as it is, "
                f"because this check changes its value to try the program on another one"
            )
        copy = tmp_path / f"{name}.py"
        copy.write_text(re.sub(pattern, f"{variable} = {value}", source, count=1, flags=re.MULTILINE))
        path = copy
    where = f"src/{name}.py" + (f" with {change[0]} = {change[1]}" if change else "")
    try:
        done = subprocess.run(
            [sys.executable, str(path)], capture_output=True, text=True, timeout=SECONDS
        )
    except subprocess.TimeoutExpired:
        raise AssertionError(
            f"{where} did not finish within {SECONDS} seconds, so a loop never ends. "
            f"Run it, stop it with Ctrl+C, and look at which value never changes"
        ) from None
    if done.returncode != 0:
        lines = [line for line in done.stderr.strip().splitlines() if line.strip()]
        error = lines[-1] if lines else "an error"
        found = re.findall(r'File "[^"]*", line (\d+)', done.stderr)
        at = f" (line {found[-1]})" if found else ""
        raise AssertionError(f"{where} stopped with {error}{at}")
    return done.stdout, where


def value(out, label):
    """Return what follows `label` at the start of a line, normalized, or None."""
    words = r"\s+".join(re.escape(word) for word in label.split())
    match = re.search(rf"^\s*{words}\s*:?\s*([^\n]*)", out, re.IGNORECASE | re.MULTILINE)
    if match is None:
        return None
    return " ".join(match.group(1).split()).upper().rstrip(".! ")


def expect(name, tmp_path, label, want, change=None):
    out, where = run(name, tmp_path, change)
    got = value(out, label)
    if got is None:
        raise AssertionError(f'{where} printed no line starting "{label}"')
    assert got == str(want).upper(), f'{where} printed "{label}: {got}", expected {want}'


def test_syntax_1(tmp_path):
    expect("syntax_1", tmp_path, "Checks until dark", 3)
    expect("syntax_1", tmp_path, "Checks until dark", 6, change=("reading", 80))


def test_syntax_2(tmp_path):
    expect("syntax_2", tmp_path, "Hours", 2)
    expect("syntax_2", tmp_path, "Minutes", 25)
    expect("syntax_2", tmp_path, "Minutes", 1, change=("total_minutes", 61))


def test_syntax_3(tmp_path):
    expect("syntax_3", tmp_path, "Flashes sent", 4)
    expect("syntax_3", tmp_path, "Flashes sent", 7, change=("flashes", 7))


def test_runtime_1(tmp_path):
    expect("runtime_1", tmp_path, "Next year", 2027)
    expect("runtime_1", tmp_path, "Next year", 2000, change=("date", '"12-31-1999"'))


def test_runtime_2(tmp_path):
    expect("runtime_2", tmp_path, "Spotlight", "GP13")
    expect("runtime_2", tmp_path, "Spotlight", "GP15", change=("choice", 1))


def test_runtime_3(tmp_path):
    expect("runtime_3", tmp_path, "Long flashes", 2)
    expect("runtime_3", tmp_path, "Long flashes", 3, change=("pattern", 10))


def test_logic_1(tmp_path):
    expect("logic_1", tmp_path, "Chase rounds", 3)
    expect("logic_1", tmp_path, "Chase rounds", 5, change=("rounds", 5))


def test_logic_2(tmp_path):
    expect("logic_2", tmp_path, "Charging trips", 3)
    expect("logic_2", tmp_path, "Charging trips", 2, change=("charge", 25))


def test_logic_3(tmp_path):
    expect("logic_3", tmp_path, "Total flashes", 16)
    expect("logic_3", tmp_path, "Total flashes", 8, change=("flashes", "[2, 2, 2, 2]"))


def test_no_todo_markers():
    left = sorted(path.name for path in SRC.glob("*.py") if "TODO" in path.read_text(encoding="utf-8"))
    assert not left, "TODO markers remain in " + ", ".join(left) + ": delete each one once that program is fixed"
