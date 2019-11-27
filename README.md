# django-flexible-manifest-staticfiles

This extendion to django.contrib.staticfiles.storage.ManifestStaticFilesStorage allows you to specify a list of file patterns that should be ignored/excluded from being versioned and added to the manifest. You can also specify it the other way around and say which files should be included.

This allows you to add versioned naming to only static files of your choosing. For example, you may want CSS and JS files to be versioned, but not fonts, images or other assets.

I've written and tested this against Django 2.2. Your mileage elsewhere may vary!

## Installation

Use pip:

```shell
pip install django-flexible-manifest-staticfiles
```

## Setup

Set in your `settings.py`:

```python
STATICFILES_STORAGE = 'django_flexible_manifest_staticfiles.storages.ForgivingManifestStaticFilesStorage'
```

## Usage

Set in your `settings.py` you can set two settings:

 - `STATICFILES_VERSIONED_INCLUDE` - This is a list of patterns you want to be included. Only files that match at least one of these patterns will be included. If you omit this setting, then all files are included by default.
 - `STATICFILES_VERSIONED_EXCLUDE` - Any file matching any of these patterns will be excluded from being versioned.

 Note that the complete path relative to the `static` directory is available for matching against.

 ## Examples

This would only version `.css` and `.js` files, but would exclude minified files:

```python
STATICFILES_VERSIONED_INCLUDE = ['.css$', '.js$']
STATICFILES_VERSIONED_EXCLUDE = ['min.css$', 'min.js$']
```

This would version all files asides from `.jpg` files:

```python
STATICFILES_VERSIONED_EXCLUDE = ['.jpg$']
```

This would only version things in your `/static/scripts`:

```python
STATICFILES_VERSIONED_INCLUDE = ['scripts/.*$']
```
