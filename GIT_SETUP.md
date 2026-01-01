# 🔧 Git Setup & Authentication Guide

## Current Status

You're setting up Git authentication to push your shopping app to GitHub.

### ✅ Completed Steps:
1. ✅ Git user configured: `LAKSHMINARASIMHATM`
2. ✅ Git email configured: `simha@example.com`
3. ✅ Logged out from old GitHub account (`23091a05c0-dotcom`)
4. 🔄 **IN PROGRESS**: Logging in with GitHub CLI

## 🎯 Current Action Required

### GitHub CLI Authentication

**Your one-time code**: `209F-ED45`

**Steps to complete**:
1. A browser window should have opened to: https://github.com/login/device
2. If not, manually open: https://github.com/login/device
3. Enter the code: `209F-ED45`
4. Login with your GitHub account: `LAKSHMINARASIMHATM`
5. Click "Authorize GitHub CLI"
6. Return to the terminal - it should show "✓ Authentication complete"

## 📝 After Authentication

Once GitHub CLI authentication is complete, you can push your code:

### Option 1: Using the existing commands

```bash
# Check if remote already exists
git remote -v

# If remote exists, remove it first
git remote remove origin

# Add the correct remote
git remote add origin https://github.com/LAKSHMINARASIMHATM/shopping-app.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Option 2: Create a new repository first

If the repository doesn't exist yet on GitHub:

```bash
# Create repository using GitHub CLI
gh repo create shopping-app --public --source=. --remote=origin

# Push code
git branch -M main
git push -u origin main
```

## 🔍 Verify Your Git Configuration

```bash
# Check Git user
git config --global user.name
# Should show: LAKSHMINARASIMHATM

# Check Git email
git config --global user.email
# Should show: simha@example.com

# Check GitHub CLI authentication
gh auth status
# Should show: Logged in to github.com account LAKSHMINARASIMHATM
```

## 🚨 Troubleshooting

### Issue: "Permission denied" or 403 error

**Cause**: Wrong GitHub account is cached in credentials

**Solution**:
```bash
# Logout and login again
gh auth logout
gh auth login
```

### Issue: "Repository not found"

**Cause**: Repository doesn't exist on GitHub

**Solution**:
```bash
# Create the repository first
gh repo create shopping-app --public --source=. --remote=origin
```

### Issue: "Authentication failed"

**Cause**: GitHub CLI not properly authenticated

**Solution**:
```bash
# Check authentication status
gh auth status

# If not logged in, login again
gh auth login
```

## 📦 Initial Git Setup (Already Done)

For reference, here's what was configured:

```bash
# Set Git user
git config --global user.name "LAKSHMINARASIMHATM"

# Set Git email
git config --global user.email "simha@example.com"

# Set credential helper
git config --global credential.helper store
```

## 🎉 Next Steps After Pushing

Once your code is pushed to GitHub:

1. **Set up GitHub Actions** (optional) - for CI/CD
2. **Configure GitHub Pages** (optional) - for frontend hosting
3. **Set up Secrets** - for environment variables:
   - `MONGO_URL`
   - `GEMINI_API_KEY`
   - `JWT_SECRET`

## 📚 Useful Git Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# View remote repositories
git remote -v

# Pull latest changes
git pull origin main

# Push changes
git push origin main

# Create and switch to new branch
git checkout -b feature-name

# View all branches
git branch -a
```

## 🔗 Repository Information

- **Repository**: `shopping-app`
- **Owner**: `LAKSHMINARASIMHATM`
- **URL**: https://github.com/LAKSHMINARASIMHATM/shopping-app
- **Branch**: `main`

---

**Need Help?** If you encounter any issues, check the troubleshooting section above or run `gh auth status` to verify your authentication.
