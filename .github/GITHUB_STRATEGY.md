# GitHub Strategy for sirene-api-client

## Overview

This document outlines our GitHub strategy for the `sirene-api-client` project, including branching model, CI/CD pipeline, release management, and community engagement.

**Project Context**:

- **Initial Release**: Version 0.1.0 marks the initial release of this client package
- **Target API**: This client package is designed for the **SIRENE API v3.11**
- **GitFlow Compliance**: We follow the complete GitFlow workflow with all required branch types and merge patterns

## Branching Strategy: GitFlow

We follow the **GitFlow** branching model (fully compliant) with two main branches:

- **`main`**: Production-ready code, always deployable
- **`develop`**: Integration branch for features, preparation for next release

### Supporting Branches (GitFlow Standard)

- **`feature/*`**: New features developed from `develop`, merged back to `develop`
- **`release/*`**: Release preparation branches from `develop`, merged to both `main` and `develop`
- **`hotfix/*`**: Emergency fixes from `main`, merged to both `main` and `develop` (keeps branches synchronized)

**Note**: This client package targets the **SIRENE API v3.11**. All development and releases maintain compatibility with this API version.

### Branch Protection Rules

- **`main` branch**:
  - Require pull request reviews (1 reviewer)
  - Require status checks to pass before merging
  - Require branches to be up to date before merging
  - Restrict pushes to main branch
  - Include administrators in restrictions

- **`develop` branch**:
  - Require pull request reviews (1 reviewer)
  - Require status checks to pass before merging

## CI/CD Pipeline

### GitHub Actions Workflow

Our CI pipeline runs on every push and pull request:

1. **Test Matrix**: Python 3.13 only (as per project requirements)
2. **Quality Gates** (via pre-commit hooks):
   - Pre-commit hooks execution (includes all quality checks)
   - Unit tests with 90%+ coverage requirement
   - Integration tests
3. **Manual Release Process**: Package building and publishing via GitHub releases

### Workflow Triggers

- **Push to `main`**: Full pipeline for validation
- **Pull Requests to `main`**: Full pipeline for validation
- **Develop Branch**: Local testing only (via pre-commit hooks)
  - Developers must run `make pre-commit-develop` before pushing
  - Weekly automated CI validation (scheduled)

### Local-First Testing Strategy

To optimize GitHub Actions usage while maintaining quality:

1. **All commits**: Pre-commit hooks run comprehensive checks locally
2. **Before pushing to develop**: Run `make pre-commit-develop`
3. **Before PR to main**: Run `make pre-commit-main`
4. **CI validation**: Only on main branch and PRs to main

**Rationale**: Our comprehensive pre-commit hooks (15+ checks including 90% coverage requirement) catch 95%+ of issues locally, making develop branch CI redundant.

## Release Management

### Version Strategy

- **Semantic Versioning**: `MAJOR.MINOR.PATCH`
- **Current Version**: 0.1.0 (Initial Release)
- **SIRENE API Version**: v3.11 (target API version)
- **Release Process**: GitFlow-based release branches (fully compliant)

### Release Workflow

1. **Feature Development**: All features developed in feature branches from `develop`
2. **Release Preparation**: Create `release/vX.Y.Z` branch from `develop`
3. **Release Testing**: Final testing and version bumping
4. **Release Merge**: Merge to `main` and create GitHub tag
5. **Manual Release**: Create GitHub release with built packages
6. **Release Integration**: Merge release branch back to `develop` (GitFlow requirement)
7. **Hotfixes**: Emergency fixes via `hotfix/vX.Y.Z` branches from `main`, merged to both `main` and `develop`

### Release Checklist

- [ ] All tests passing
- [ ] Coverage ≥ 90%
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Version bumped in pyproject.toml
- [ ] Security scan clean
- [ ] Performance benchmarks acceptable

## Community Engagement

### Issue Management

- **Bug Reports**: Use bug report template
- **Feature Requests**: Use feature request template
- **Questions**: Use Q&A template or Discussions

### Pull Request Process

1. **Fork & Branch**: Create feature branch from `develop`
2. **Development**: Follow TDD principles
3. **Testing**: Ensure all tests pass locally
4. **Documentation**: Update docs for new features
5. **Review**: Address reviewer feedback
6. **Merge**: Squash and merge to `develop`

### Code Review Guidelines

- **TDD Compliance**: All new code must have tests first
- **Coverage**: Maintain 90%+ test coverage
- **Documentation**: Public APIs must be documented
- **Security**: Security-sensitive code requires additional review

## Security Strategy

### Security Measures

- **Dependency Scanning**: Automated via Dependabot
- **Code Scanning**: GitHub CodeQL analysis
- **Secret Scanning**: Prevent credential leaks
- **Security Advisories**: Coordinated disclosure process

### Vulnerability Response

1. **Assessment**: Evaluate severity and impact
2. **Patches**: Develop fixes in private branches
3. **Disclosure**: Coordinate with security team
4. **Release**: Deploy security updates

## Documentation Strategy

### Documentation Types

- **API Documentation**: Auto-generated from docstrings
- **User Guides**: Step-by-step tutorials
- **Developer Docs**: Contributing guidelines
- **Architecture**: System design decisions

### Documentation Maintenance

- **Automated Updates**: CI updates API docs
- **Version Control**: Docs versioned with code
- **Review Process**: Docs reviewed with code changes

## Monitoring & Analytics

### Repository Metrics

- **Code Quality**: Coverage, complexity metrics
- **Community Health**: Issue/PR response times
- **Security**: Vulnerability counts, fix times
- **Performance**: Build times, test execution

### Key Performance Indicators

- **Build Success Rate**: > 95%
- **Test Coverage**: ≥ 90%
- **Issue Resolution**: < 48 hours for critical bugs
- **PR Review Time**: < 24 hours for first review

## Future Enhancements

### Planned Improvements

- [ ] **PyPI Publication**: Automated package publishing (see PyPI TODO)
- [ ] **GitHub Pages**: Documentation hosting (when documentation is ready)
- [ ] **Code Coverage**: Integration with Codecov
- [ ] **Performance Testing**: Automated benchmarks
- [ ] **Docker Support**: Containerized testing

### PyPI Publication Strategy (TODO)

**Status**: Not yet implemented - using GitHub releases for distribution

**Current Approach**:

- Manual GitHub releases with built packages
- Comprehensive release process documented in [RELEASE_PROCESS.md](RELEASE_PROCESS.md)
- Local package building using `make build`

**Future PyPI Requirements**:

- PyPI account creation
- API token generation
- GitHub Secrets configuration
- Automated publishing workflow

**Implementation Plan**:

1. Create PyPI account for `karibu-earth` organization
2. Generate API token with appropriate permissions
3. Add `PYPI_API_TOKEN` to GitHub repository secrets
4. Extend manual release process to include PyPI publishing
5. Test publishing process with test PyPI first

**Security Considerations**:

- Use scoped API tokens
- Rotate tokens regularly
- Monitor publishing activity
- Implement signing for packages

## Maintenance Schedule

### Regular Tasks

- **Weekly**: Review and merge Dependabot PRs
- **Monthly**: Update dependencies and security patches
- **Quarterly**: Review and update documentation
- **Annually**: Review branching strategy and CI/CD pipeline

### Emergency Procedures

- **Security Incidents**: Follow security response playbook
- **Build Failures**: Immediate investigation and hotfix
- **Dependency Issues**: Rapid assessment and resolution

## Contact & Support

- **Technical Issues**: GitHub Issues
- **Security Concerns**: Security advisories
- **General Questions**: GitHub Discussions
- **Commercial Support**: Contact karibu-earth team

---

*This strategy document is living and will be updated as the project evolves.*
