# Getting a GitHub Token

To use the Python comment bot script, you need a GitHub Personal Access Token.

## Steps to create a GitHub Token:

1. Go to GitHub Settings: https://github.com/settings
2. Click on "Developer settings" in the left sidebar
3. Click on "Personal access tokens"
4. Click on "Tokens (classic)"
5. Click "Generate new token" then "Generate new token (classic)"
6. Give your token a descriptive name (e.g., "Auto Comment Bot")
7. Select the scopes needed:
   - `repo` (to access repositories)
   - `write:discussion` (to comment on issues)
8. Click "Generate token"
9. Copy the token immediately (it won't be shown again)

## Setting the token for the Python script:

```bash
export GITHUB_TOKEN='your_token_here'
```

## Security notes:
- Never share your token publicly
- Store it securely
- Consider using GitHub Actions secrets for automation workflows