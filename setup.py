#!/usr/bin/env python

from distutils.core import setup


setup(name='django-headcrumbs',
      version='2014.12.001',

      description='Smart and easy-to-use breadcrumbs for Django',
      long_description='''
          Breadcrumbs for Django_ that are not going to eat your brains!

          See README_ for more details.

          .. _Django: https://www.djangoproject.com/
          .. _README: https://github.com/kirelagin/django-headcrumbs/blob/master/README.md
      ''',


      author='Kirill Elagin',
      author_email='kirelagin@gmail.com',

      url='https://github.com/kirelagin/django-headcrumbs',

      classifiers = ['Development Status :: 5 - Production/Stable',
                     'Environment :: Web Environment',
                     'Framework :: Django',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 3',
                     'Topic :: Software Development :: Libraries',
                    ],
      keywords = ['Django', 'breadcrumbs'],

      packages = ['headcrumbs'],
      package_data = {
        'headcrumbs': [
            'templates/crumbs.html',
        ],
      },
     )
