# Change Log

## [1.0.32] 2025-05-12
### [Django Soft UI Dashboard](https://app-generator.dev/product/soft-ui-dashboard/django/) Changes

- CONFIG.Settings/SECRET_KEY: remove randomness if not specified 

## [1.0.31] 2025-04-18
[Django Soft UI Dashboard](https://app-generator.dev/product/soft-ui-dashboard/django/)

- Update RM, Features Section:
  - Simple, Easy-to-Extend codebase
  - [Soft UI Dashboard](https://app-generator.dev/product/soft-ui-dashboard/) 
  - [Bootstrap](https://app-generator.dev/docs/templates/bootstrap.html) CSS Styling 
  - Dynamic Tables - read [docs](https://app-generator.dev/docs/developer-tools/dynamic-datatables.html)
  - Dynamic API - read [docs](https://app-generator.dev/docs/developer-tools/dynamic-api.html)
  - Charts
  - [Django CLI Package](https://app-generator.dev/docs/developer-tools/django-cli/index.html)
      - [Commit/rollback Git Changes](https://app-generator.dev/docs/developer-tools/django-cli/git-interface.html)
      - `Backup & restore DB`
      - [Interact with Django Core](https://app-generator.dev/docs/developer-tools/django-cli/query-django.html)
      - `Manage Environment`
      - `Manage Dependencies`
  - Session-based Authentication, Password recovery
  - DB Persistence: SQLite (default), can be used with MySql, PgSql
  - Docker, CI/CD for Render
  - [Vite](https://app-generator.dev/docs/technologies/vite/index.html) for assets management 

## [1.0.30] 2025-04-15
[Django Soft UI Dashboard](https://app-generator.dev/product/soft-ui-dashboard/django/)

- New Apps
  - Dynamic DataTables
  - Dynamic API
  - Charts
- Jazzmin for ADMIN Section  

## [1.0.29] 2024-12-16
### Changes

- Preselect the design in the Generator:
  - [Django App Generator - Soft Design](https://app-generator.dev/tools/django-generator/soft/)

## [1.0.28] 2024-12-15
### Changes

> Mention [Django App Generator](https://app-generator.dev/tools/django-generator/) Service:

- Access the [App Generator](https://app-generator.dev/tools/django-generator/) page
- Select the preferred design
- (Optional) Design Database: edit models and fields
- (Optional) Edit the fields for the extended user model
- (Optional) Enable OAuth for GitHub
- (Optional) Add Celery (async tasks)
- (Optional) Enable Dynamic API Module
- Docker Scripts
- Render CI/Cd Scripts

**The generated Django project is available as a ZIP Archive and also uploaded to GitHub.**

## [1.0.27] 2024-12-02
### Changes

- Update Media Files
  - [Django Soft Dashboard](https://app-generator.dev/product/soft-ui-dashboard/django/)
  - [Django Soft Dashboard PRO](https://app-generator.dev/product/soft-ui-dashboard-pro/django/)

## [1.0.26] 2024-11-28
### Changes

> Added **Deploy on Render** Button

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy) 

## [1.0.25] 2024-11-28
### Changes

- Bump UI Theme Version

## [1.0.24] 2024-11-26
### Changes

> Update RM Links

- 👉 [Django Soft UI Dashboard](https://app-generator.dev/product/soft-ui-dashboard/django/) - `Product Page`
- 👉 [Django Soft UI Dashboard Documentation](https://app-generator.dev/docs/products/django/soft-ui-dashboard/index.html) - `Complete Information` and Support Links
  - [Getting Started with Django](https://app-generator.dev/docs/technologies/django/index.html) - a `comprehensive tutorial`
  - `Configuration`: Install Dependencies, Prepare Environment, Setting up the Database 
  - `Start with Docker`
  - `Manual Build`
  - `Start the project`
  - `Deploy on Render`
  
## [1.0.23] 2024-05-18
### Changes

- Updated DOCS (readme)
  - [Custom Development](https://appseed.us/custom-development/) Section
  - [CI/CD Assistance for AWS, DO](https://appseed.us/terms/#section-ci-cd)

## [1.0.22] 2024-03-05
### Changes

- Update [Custom Development](https://appseed.us/custom-development/) Section
  - New Pricing: `$3,999`

## [1.0.21] 2024-03-04
### Changes

- Deprecate `distutils`
  - use `str2bool`
- Update Deps 
  - `requirements.txt`  
- Update README: [PRO Version](https://appseed.us/product/soft-ui-dashboard-pro/django/), List features
  - `API`, **Charts** 
  - **DataTables** (Filters, Export)
  - **Celery**
  - **Media Files Manager**
  - **Extended User Profiles**

## [1.0.20] 2023-02-14
### Changes

- Update [Custom Development](https://appseed.us/custom-development/) Section
- Minor Changes (readme)

## [1.0.19] 2023-10-21
### Changes

- Update Dependencies 
- Update README 

## [1.0.18] 2023-04-06
### Changes

- Bump Design: [Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard) `v1.0.12`

## [1.0.17] 2023-04-04
### Changes

- Added Local Templates and Static
- Added Gulp Tooling
- DOCS Update (readme)

## [1.0.16] 2023-02-28
### Changes

- Bump Design: [Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard) `v1.0.10`

## [1.0.15] 2023-01-29
### Changes

- Bump Design: [Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard) `v1.0.9`

## [1.0.14] 2023-01-29
### Changes

- Bump Design: [Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard) `v1.0.8`
- DOCS Update (readme). New sections:
  - `How to customize the theme`
  - Render deployment
- Configure the project to use `home/templates`
- Added `custom_footer` sample

## [1.0.13] 2023-01-09
### Changes

- Move to theme-based pattern
  - [Django Admin Soft](https://github.com/app-generator/django-admin-soft-dashboard)
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

## [1.0.12] 2022-09-18
### Improvements

- Dynamic DataTables:
  - Server-Side Pagination, Search, Export 

## [1.0.11] 2022-09-17
### Improvements

- API Generator 
  - the code is generated on top of DRF
  - Mutating requests secured by JWT

## [1.0.10] 2022-09-17
### Improvements

- Added **Github OAuth** via AllAuth. requires in `.env`:
  - `GITHUB_ID`=<YOUR_GITHUB_ID>
  - `GITHUB_SECRET`=<YOUR_GITHUB_SECRET>

## [1.0.9] 2022-09-17
### Improvements

- Bump Codebase & UI version
- Docker scripts update

## [1.0.8] 2022-06-21
### Improvements

- UI Update: `Soft UI Dashboard` v1.0.6
- Enhanced version:
  - `Dark Mode`

## [1.0.7] 2022-05-25
### Improvements

- Built with [Soft UI Dashboard Generator](https://appseed.us/generator/soft-ui-dashboard/)
  - Timestamp: `2022-05-25 10:16`
- Added CDN/Static Server management
  - `ASSETS_ROOT` env variable

## [1.0.6] 2022-05-24
### Improvements 

- UI Update: `Soft UI Dashboard` v1.0.5
  - upgrade Bootstrap version to v5.1.3
  - upgrade ChartJs plugin version to v3.7.1
  - fix running 'npm install' issue
  - fix SCSS compiling issues
  - update sidebar height
  - fix sidebar button on Safari
  - update dropdown text on RTL page
  - fix navbar scroll error on example pages

## [1.0.5] 2022-01-16
### Improvements

- Bump Django Codebase to [v2stable.0.1](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Dependencies update (all packages) 
  - Django==4.0.1
- Settings update for Django 4.x
  - `New Parameter`: CSRF_TRUSTED_ORIGINS
    - [Origin header checking isn`t performed in older versions](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins)  

## [1.0.4] 2021-12-09
### Improvements

- Bump UI: Soft UI Dashboard **v1.0.3**

## [1.0.3] 2021-09-20
### Improvements 

- Bump Django Codebase to [v2.0.4](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Codebase update
  - `assets` & `templates` moved to `apps` folder
  - `apps/base` renamed to `apps/home`
  
## [1.0.2] 2021-09-08
### Improvements & Fixes

- Bump Django Codebase to [v2.0.2](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
  - Dependencies update (all packages)
    - Use Django==3.2.6 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update
- Tooling: added scripts to recompile the SCSS files
  - `config/static/assets/` - gulpfile.js
  - `config/static/assets/` - package.json
  - `Update README` - [Recompile SCSS](https://github.com/app-generator/django-soft-ui-dashboard#recompile-css) (new section)
- Fixes: 
  - Patch 500 Error when authenticated users access `admin` path (no slash at the end)
  - Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker 

## [1.0.1] 2020-05-28
### Remove Media & Minor Fixes

- Patch `logout` link 
- Delete useless `media` directory

## [1.0.0] 2020-05-28
### Initial Release

- Codebase: [Django Dashboard](https://github.com/app-generator/boilerplate-code-django-dashboard) v1.0.4
- UI: [Jinja Soft UI](https://github.com/app-generator/jinja-soft-ui-dashboard) v1.0.0
- UI Kit: Soft UI Dashboard v1.0.1
