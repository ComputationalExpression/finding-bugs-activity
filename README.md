# Activity 4: Finding Bugs

|Item |       |
|:----|:------|
|Released |Wednesday, October 7, in class |
|Due |Monday, October 12, 9:50am |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

There are nine short programs, each one taken from a lab or a session you have already done,
and each one has exactly one bug in it. Find and fix the bug in each one. Three stop before they
run, three crash partway through, and three run to the end and print the wrong answer.

Everything here comes from the Week 7 debugging session and the weeks before it. If a step
confuses you, please ask about it while you are still in the room.

## Course learning outcomes

This activity addresses the following course learning outcomes:

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

**CLO 3.** Analyze and suggest revisions to existing Python language code to add functionality
or repair defects.

Specifically, by the end of this activity you should be able to:

* tell a syntax error, a runtime error, and a logic error apart
* read an error message from its last line, and find the line it points at
* find a logic error by comparing what a program prints with what it should print
* stop a loop that never ends, and find the value that never changes

## The programs

Each program prints one line at the end that says whether it is fixed:

|File |Kind of bug |Prints when fixed |
|:----|:-----------|:-----------------|
|`src/syntax_1.py` |Syntax |`Checks until dark: 3` |
|`src/syntax_2.py` |Syntax |`Hours: 2`, then `Minutes: 25` |
|`src/syntax_3.py` |Syntax |`Flashes sent: 4` |
|`src/runtime_1.py` |Runtime |`Next year: 2027` |
|`src/runtime_2.py` |Runtime |`Spotlight: GP13` |
|`src/runtime_3.py` |Runtime |`Long flashes: 2` |
|`src/logic_1.py` |Logic |`Chase rounds: 3` |
|`src/logic_2.py` |Logic |`Charging trips: 3` |
|`src/logic_3.py` |Logic |`Total flashes: 16` |

The checks also run every program with its first value changed, so keep that first line where
it is.

## Getting started

Work through the files in the order of the table. Run each one, read what happens, fix the
one line that causes it, and run it again:

```text
uv run python src/syntax_1.py
```

A loop that never ends keeps printing, or sits waiting. Press `Ctrl+C` in the terminal to stop
it.

When a bug will not show itself, use duck debugging. Explain the program to your tiny duck one
line at a time, saying what each line should do and what it actually does; the line where those
two stop matching is usually the bug.

Delete the `TODO` line at the top of each file once that program prints the right line.

## Evaluation

In-class activities are graded on completion and contribute to the **In-Class Activities**
category on the syllabus (10 points, averaged across the semester). This activity is worth one
activity grade. What is graded is the attempt, not whether every value comes out right.

|Level |What it looks like |
|:-----|:------------------|
|**Complete** |At least half of the activity is done |
|**Partial** |Less than half is done, but something beyond the starter was committed |
|**Incomplete** |Nothing was changed |

Run the automated checks yourself, as many times as you like, from the top folder of this
repository rather than from inside `src`:

```text
uv run gatorgrade --config gatorgrade.yml
```

Each check's description says where to look when it fails. Under a failed check, gatorgrade
also prints a `uv run pytest ...` command. Run it: the last lines name the file, say whether it
stopped with an error, never finished, or printed the wrong value, and quote the error.

> [!NOTE]
> Automated results are preliminary. Your instructor sets the final grade.

## Submitting

Commit and push often. The last version pushed before the deadline is the one that gets
graded.

**In the terminal:**

```text
git add src
git commit -m "Fix the nine bugs"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it, which is `git add`
2. Type a message in the box at the top, then click the checkmark, which is `git commit`
3. Click **Sync Changes** (or the up arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are actually
there.

If you need more time, apply a late token with [this form](https://forms.gle/3nGbpaNrG96DpLLdA).
