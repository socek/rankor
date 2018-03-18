"""
About this project

"""

from setuptools import find_packages
from setuptools import setup

setup(
    name='rankor',
    version='0.1',
    description='',
    packages=find_packages(),
    install_requires=[
        'pyramid', 'SQLAlchemy', 'psycopg2', 'PyYAML', 'alembic', 'raven',
        'celery', 'marshmallow',
        'sapp==0.1'
    ],
    dependency_links=[
        'git://github.com/socek/qapla/@pluginable#egg=sapp-0.1'
    ],
    tests_require=['coverage', 'freezegun', 'pytest', 'pytest-cov', 'WebTest'],
    long_description=__doc__,
    author='Dominik "Socek" Długajczyk',
    author_email='msocek@gmail.com',
    license='MIT',
    zip_safe=False,
    url='http://github.com/socek/rankor',
    keywords=['pet'],
    entry_points={
        'paste.app_factory': ['main = rankor.application.startpoints:uwsgi'],
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
