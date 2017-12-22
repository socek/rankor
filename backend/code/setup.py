"""
Clearcode Ads
-------------

About this project

"""

from setuptools import find_packages
from setuptools import setup

setup(
    name='mypet',
    version='0.1',
    description='',
    packages=find_packages(),
    install_requires=[
        'pyramid', 'SQLAlchemy', 'psycopg2', 'PyYAML', 'alembic', 'raven',
        'celery', 'marshmallow', 'sapp==0.1'
    ],
    dependency_links=[
        'git://github.com/socek/qapla/@eb2ab448ce7f176991e12c64faff99a90547de02#egg=sapp-0.1'
    ],
    tests_require=['coverage', 'freezegun', 'pytest', 'pytest-cov', 'WebTest'],
    long_description=__doc__,
    author='Dominik "Socek" Długajczyk',
    author_email='msocek@gmail.com',
    license='MIT',
    zip_safe=False,
    # url='',
    keywords=['pet'],
    entry_points={
        'paste.app_factory': ['main = mypet.application.startpoints:uwsgi'],
    },
    classifiers=[
        'Development Status :: 4 - Beta', 'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
)
