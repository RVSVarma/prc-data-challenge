# PRC Data Challenge

Python exploration of flight and airport movement data for the PRC Data Challenge.

`PRCData.py` loads the training dataset, reports column types, summary statistics
and missing values, and drops rows containing missing values in memory.

## Run locally

From PowerShell in this project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe PRCData.py
```

Place `training_2025-01-01_2025-02-01.parquet` in the project root before running.
Datasets are excluded from Git; obtain the training file separately.

## Git workflow

Before starting work, once the GitHub remote is configured and the working tree
is clean:

```powershell
git pull --ff-only
```

After completing a meaningful change:

```powershell
git status
git diff
git add README.md PRCData.py requirements.txt .gitignore
git diff --cached
git commit -m "Describe the change"
git push
```

Adjust the `git add` file list to include the files you intentionally changed.
Review staged changes before committing. Commit and push at the end of each
completed task so GitHub holds the latest completed work.

For larger changes, use a branch and open a pull request on GitHub:

```powershell
git switch -c feature/short-description
# Edit, review, stage, and commit your changes.
git push -u origin feature/short-description
```

## Connect to GitHub

Create an empty repository called `prc-data-challenge` in your GitHub account,
then run the following with your account name substituted for `YOUR_USERNAME`:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/prc-data-challenge.git
git push -u origin main
```

Choose the repository visibility when creating it. Public repositories are
visible to everyone. Authentication is handled by your Git credential manager.
