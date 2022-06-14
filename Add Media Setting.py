# Step No 1: Go to "Settings.py" file and add the following code.

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Step No 2: Go to "urls.py" file and add the following code.

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('university.urls')),
]

urlpatterns += static (settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)