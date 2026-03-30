#!/usr/bin/env python3
"""
Test script to demonstrate the comment bot functionality.
Note: This requires GITHUB_TOKEN environment variable to be set.
"""

import os
import subprocess

# Test the comment bot script
print("Testing the comment bot...")
print("=" * 50)

# Check if GITHUB_TOKEN is set
if not os.environ.get('GITHUB_TOKEN'):
    print("Note: GITHUB_TOKEN environment variable is not set.")
    print("The script will work if you set it before running.")
    print("Example: export GITHUB_TOKEN='your_token_here'")
else:
    print("GITHUB_TOKEN is set. Ready to test!")

print("\nTo test the comment bot manually:")
print("1. First, set your GitHub token:")
print("   export GITHUB_TOKEN='your_personal_access_token'")
print("2. Run the comment bot:")
print("   python comment_bot.py 1 'Test comment from Python script!'")
print("\nThe GitHub Actions workflow is already set up to automatically")
print("comment 'Thank you for your contribution!' on all new issues.")