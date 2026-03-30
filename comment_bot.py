#!/usr/bin/env python3
"""
Simple GitHub automation script that comments on issues.
This can be run manually or integrated into CI/CD pipelines.
"""

import os
import sys
import requests

def comment_on_issue(issue_number, comment_text):
    """
    Add a comment to a GitHub issue.
    
    Args:
        issue_number: The issue number to comment on
        comment_text: The comment text to add
    """
    # GitHub API endpoint for adding comments
    github_token = os.environ.get('GITHUB_TOKEN')
    repo = os.environ.get('GITHUB_REPOSITORY', 'CaSTSubmission/auto-comment-bot-x')
    
    if not github_token:
        print("Error: GITHUB_TOKEN environment variable is required")
        return
    
    api_url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    data = {
        'body': comment_text
    }
    
    response = requests.post(api_url, headers=headers, json=data)
    
    if response.status_code == 201:
        print(f"Successfully added comment to issue #{issue_number}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python comment_bot.py <issue_number> <comment_text>")
        sys.exit(1)
    
    issue_number = int(sys.argv[1])
    comment_text = sys.argv[2]
    
    comment_on_issue(issue_number, comment_text)