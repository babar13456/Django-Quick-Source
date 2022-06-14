# Step No 1: Create folder name "static" in "settings.py" file.

# Step No 2: Go to settings.py and add the following code for static files

# Step No 3: Then Write in CMD: python manage.py collectstatic

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')