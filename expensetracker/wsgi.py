"""
WSGI config for expensetracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


# import nltk
# nltk.download('stopwords')  # ✅ Download on server start




# this below extra added 
# Set a local nltk_data folder in your project directory
nltk_data_dir = os.path.join(os.path.dirname(__file__), 'nltk_data')

# Create directory if not exist
os.makedirs(nltk_data_dir, exist_ok=True)

# Append to nltk data search paths so it looks here first
nltk.data.path.append(nltk_data_dir)

# Try to find stopwords corpus, if missing download it here
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', download_dir=nltk_data_dir)









os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expensetracker.settings')

application = get_wsgi_application()


###################################################################################################################################################################
