import os
import sys

# Убедитесь, что этот путь соответствует пути к вашему проекту Django
sys.path.append('/home/h541054/test.macsart.ru/www')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsadbekProject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
