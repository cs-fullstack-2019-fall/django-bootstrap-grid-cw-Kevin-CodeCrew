from django.shortcuts import render


# Generic landing page
def index(req):
    return render(req, 'django_bootstrap_app/index.html', {})


# Generic page handler
def generic_view(req, pgnum):
    pgnum_url = f'django_bootstrap_app/pg{pgnum}.html'
    return render(req, pgnum_url, {'pgnum': pgnum})
