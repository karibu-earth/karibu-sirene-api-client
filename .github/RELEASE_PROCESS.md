# Release Process Guide

This document provides a comprehensive guide for creating releases of the `sirene-api-client` package using GitHub's manual release system.

**Project Context**:

- **Initial Release**: Version 0.1.0 marks the initial release of this client package
- **Target API**: This client package is designed for the **SIRENE API v3.11**
- **GitFlow Compliance**: This process follows the complete GitFlow workflow (fully compliant)

## Prerequisites

Before creating a release, ensure you have:

- **Git access** to the repository with push permissions
- **uv** installed for package building (`pip install uv`)
- **GitHub access** with release creation permissions
- **Clean working directory** with all changes committed
- **All tests passing** locally and in CI

## Version Numbering

Follow [Semantic Versioning](https://semver.org/) (SemVer):

- **MAJOR** (X.0.0): Breaking changes that are not backwards compatible
- **MINOR** (X.Y.0): New features that are backwards compatible
- **PATCH** (X.Y.Z): Bug fixes that are backwards compatible

### Pre-release Versions

For testing purposes, use pre-release identifiers:

- **Alpha**: `v0.2.0-alpha.1`
- **Beta**: `v0.2.0-beta.1`
- **Release Candidate**: `v0.2.0-rc.1`

## Pre-Release Checklist

Before creating any release, verify:

- [ ] All tests pass (`make test`)
- [ ] Coverage ≥ 90% (`make coverage-report`)
- [ ] Code quality checks pass (`make lint`, `make type-check`)
- [ ] Security scan clean (`make security`)
- [ ] Documentation updated (README.md, docstrings)
- [ ] CHANGELOG.md updated with new version
- [ ] Version bumped in `pyproject.toml`
- [ ] No sensitive data in commits
- [ ] All dependencies up to date
- [ ] Performance benchmarks acceptable

## GitFlow Release Workflow

This process follows **GitFlow** best practices (fully compliant):

- **`develop`** = Integration branch for features
- **`main`** = Production-ready code only
- **Release branches** = Created from `develop`, merged to both `main` and `develop`
- **Hotfix branches** = Created from `main`, merged to both `main` and `develop` (keeps branches synchronized)
- **`--no-ff`** = Preserves branch history for better traceability

## Step-by-Step Release Workflow

### Step 1: Prepare Release Branch (GitFlow)

```bash
# Ensure develop branch is up to date
git switch develop
git pull origin develop

# Create release branch from develop (GitFlow standard)
git switch -c release/v0.2.0
```

### Step 2: Update Version and Documentation

```bash
# Update version in pyproject.toml
# Example: Change from version = "0.1.0" to version = "0.2.0" (or "1.0.0" for first stable release)
# Note: Version 0.1.0 is the initial release targeting SIRENE API v3.11

# Update CHANGELOG.md
# Move items from [Unreleased] to new version section
# Add release date: ## [0.2.0] - 2024-01-15
```

### Step 3: Final Testing

```bash
# Run comprehensive test suite
make test

# Run all quality checks
make pre-commit-run
```

### Step 4: Commit Release Changes

```bash
# Commit version changes
git add pyproject.toml CHANGELOG.md
git commit -m "Bump version to v0.2.0"

# Push release branch
git push origin release/v0.2.0
```

### Step 5: Build Package

```bash
# Clean previous builds
make clean

# Build distribution packages
make build

# Verify build artifacts
ls -la dist/
# Should show: sirene_api_client-0.2.0-py3-none-any.whl
#              sirene_api_client-0.2.0.tar.gz
```

### Step 6: Merge to Main (GitFlow Production Release)

```bash
# Switch to main branch
git checkout main
git pull origin main

# Merge release branch to main (production release)
git merge --no-ff release/v0.2.0

# Create annotated tag
git tag -a v0.2.0 -m "Release v0.2.0

- Added new SIRENE API features
- Fixed coordinate conversion bugs
- Updated documentation
- See CHANGELOG.md for full details"

# Push main branch and tag
git push origin main
git push origin v0.2.0
```

### Step 7: Create GitHub Release

1. **Navigate to GitHub Releases**:
   - Go to repository → Releases → Create a new release

2. **Select Tag**:
   - Choose tag: `v0.2.0`
   - Set release title: `Release v0.2.0`

3. **Add Release Notes**:

   ``` markdown
   ## What's New in v0.2.0

   ### Added
   - New SIRENE API endpoint support
   - Enhanced ETL service capabilities
   - Improved error handling

   ### Fixed
   - Coordinate conversion accuracy issues
   - Memory optimization for large datasets
   - Documentation typos

   ### Changed
   - Updated dependencies for security
   - Improved async performance

   ## Full Changelog

   See [CHANGELOG.md](https://github.com/karibu-earth/sirene-api-client/blob/main/CHANGELOG.md) for complete details.

   ```

4. **Upload Artifacts**:

   - Upload both files from `dist/` directory
   - `sirene_api_client-0.2.0-py3-none-any.whl`
   - `sirene_api_client-0.2.0.tar.gz`

5. **Publish Release**:
   - Check "Set as the latest release" if this is the newest version
   - Click "Publish release"

### Step 8: Verification

```bash
# Test installation from release artifacts
pip install --force-reinstall sirene_api_client-0.2.0-py3-none-any.whl

# Verify installation
python -c "import sirene_api_client; print(sirene_api_client.__version__)"

# Test basic functionality
python -c "from sirene_api_client import SireneClient; print('Import successful')"
```

### Step 9: Merge Back to Develop (GitFlow Integration)

```bash
# Switch to develop branch
git checkout develop
git pull origin develop

# Merge release branch back to develop (GitFlow standard)
git merge --no-ff release/v0.2.0

# Push updated develop branch
git push origin develop

# Clean up release branch
git branch -d release/v0.2.0
git push origin --delete release/v0.2.0
```

## Hotfix Process (GitFlow Compliant)

For urgent bug fixes that need immediate deployment to production:

**Note**: This client package targets the **SIRENE API v3.11**. Hotfixes should maintain compatibility with this API version.

### Step 1: Create Hotfix Branch

```bash
# Create hotfix branch from main
git checkout main
git pull origin main
git checkout -b hotfix/v0.1.1
```

### Step 2: Apply Fix

```bash
# Make minimal changes to fix the issue
# Update CHANGELOG.md with fix details
# Update version in pyproject.toml
```

### Step 3: Fast-Track Release

```bash
# Skip full testing cycle for critical fixes
make test  # Run tests only

# Commit and tag
git add .
git commit -m "Hotfix: Fix critical bug in v0.1.1"
git tag -a v0.1.1 -m "Hotfix v0.1.1 - Critical bug fix"
git push origin hotfix/v0.1.1
git push origin v0.1.1
```

### Step 4: Merge Back to Main (GitFlow Production)

```bash
# Merge hotfix back to main
git checkout main
git pull origin main
git merge --no-ff hotfix/v0.1.1
git push origin main
```

### Step 5: Merge Back to Develop (GitFlow Integration)

**Critical**: Hotfixes must be merged to both `main` and `develop` to keep branches synchronized. This is a GitFlow requirement.

```bash
# Merge hotfix back to develop (GitFlow standard)
git checkout develop
git pull origin develop
git merge --no-ff hotfix/v0.1.1
git push origin develop

# Clean up hotfix branch
git branch -d hotfix/v0.1.1
git push origin --delete hotfix/v0.1.1
```

## Rollback Procedures

### Emergency Rollback

If a release has critical issues:

1. **Immediate Response**:
   - Mark release as "pre-release" on GitHub
   - Add warning to release notes
   - Notify users via GitHub issues/discussions

2. **Issue Assessment**:
   - Evaluate impact and root cause
   - Document the problem
   - Plan fix timeline

3. **Fix Development**:
   - Create hotfix branch
   - Develop and test fix
   - Follow hotfix process above

4. **Re-release**:
   - Create new patch version
   - Deploy corrected version
   - Communicate fix to users

## Post-Release Tasks

After successful release:

- [ ] Merge release branch back to develop (Step 9) - **GitFlow requirement**
- [ ] Clean up release branch (Step 9)
- [ ] Update project status in team channels
- [ ] Notify stakeholders of new release
- [ ] Monitor GitHub issues for user feedback
- [ ] Update any external documentation
- [ ] Archive release artifacts locally
- [ ] Update deployment scripts if applicable
- [ ] Schedule next release planning

**Note**: For hotfixes, ensure both `main` and `develop` branches are updated (Step 5 of Hotfix Process) to maintain GitFlow compliance.

## Troubleshooting

### Common Issues

**Build Fails**:

```bash
# Clean and rebuild
make clean
make build
```

**Tag Already Exists**:

```bash
# Delete local tag
git tag -d v0.2.0
# Delete remote tag
git push origin :refs/tags/v0.2.0
# Recreate tag
git tag -a v0.2.0 -m "Release v0.2.0"
```

**Upload Fails**:

- Check file sizes (GitHub has 2GB limit)
- Verify file permissions
- Try uploading one file at a time

**Installation Test Fails**:

```bash
# Check Python version compatibility
python --version
# Verify package integrity
pip check sirene-api-client
```

### Getting Help

- **Documentation**: Check README.md and CONTRIBUTING.md
- **Issues**: Search existing GitHub issues
- **Team**: Contact Francesco Portigliotti for release questions
- **Emergency**: Use hotfix process for critical issues

## Best Practices

1. **Test Everything**: Always run full test suite before release
2. **Document Changes**: Keep CHANGELOG.md comprehensive and clear
3. **Version Consistently**: Use semantic versioning strictly
4. **Tag Properly**: Use annotated tags with descriptive messages
5. **Verify Installation**: Always test package installation
6. **Communicate Changes**: Write clear release notes
7. **Monitor Feedback**: Watch for user issues after release
8. **Plan Ahead**: Schedule releases during business hours
9. **Backup Artifacts**: Keep local copies of release packages
10. **Security First**: Never release with known security issues

## Release Schedule

- **Major Releases**: Quarterly (planned breaking changes)
- **Minor Releases**: Monthly (new features)
- **Patch Releases**: As needed (bug fixes)
- **Hotfixes**: Immediate (critical issues)

## Contact Information

- **Release Manager**: Francesco Portigliotti
- **Technical Lead**: Francesco Portigliotti
- **Emergency Contact**: Use GitHub issues with "urgent" label
