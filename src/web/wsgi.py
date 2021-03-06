"""
WSGI config for web project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os, sys

import site

# need to add virtualenv path
# site.addsitedir('/mnt/code/meampy/lib/python2.7/site-packages')
# site.addsitedir('/mnt/code/meampy/lib/python2.7/dist-packages')
site.addsitedir('/home/anafora/anafora_venv/lib/python3.7/site-packages')

#activate virtualenv
# activate_env=os.path.expanduser("/mnt/code/meampy/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))

root_path = '/home/anafora/git/anafora3'

if os.path.join(root_path,'src') not in sys.path:
    sys.path.append(os.path.join(root_path,'src'))
    sys.path.append(os.path.join(root_path,'src/web'))

os.environ["DJANGO_SETTINGS_MODULE"] =  "web.settings"

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

