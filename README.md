# Automated Comment Bot

A repository to test GitHub automation for adding comments to issues.

## Setup

This repository contains two approaches for automating comments on GitHub issues:

### 1. GitHub Actions Workflow (.github/workflows/auto-comment.yml)
This workflow automatically adds a "Thank you for your contribution!" comment to any new issue opened in this repository.

### 2. Python Script (comment_bot.py)
A Python script that can be run manually or integrated into other automation systems to comment on issues.

## Testing

To test the automation:
1. Create new issues with different titles
2. The GitHub Actions workflow should automatically comment on each new issue
3. You can also run the Python script manually with: `python comment_bot.py <issue_number> <comment_text>`

## Requirements
For the Python script: `pip install requests`