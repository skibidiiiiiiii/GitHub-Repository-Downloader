# GitHub Repository Downloader

This Python script allows you to download all repositories of a given GitHub user and save them in a specified directory. Each repository is extracted into its own folder with the same name.

## Features
- Downloads all repositories for a specific GitHub user.
- Automatically organizes repositories into folders by their names.
- Supports authentication with a personal GitHub token to bypass API rate limits.
- Extracts repository contents directly from GitHub's ZIP archives.

## Prerequisites
- Python 3.6 or later.
- Required libraries:
  - `requests`
  - `tqdm`

You can install the dependencies with:
```bash
pip install requests tqdm
