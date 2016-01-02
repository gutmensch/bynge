from setuptools import setup, find_packages

# This is the distribute flavour of setuptools.
# See:
#   http://packages.python.org/distribute/
#   http://guide.python-distribute.org/
#   http://flask.pocoo.org/docs/patterns/distribute/#distribute-deployment

setup(
    name='bynge',
    version='0.1',
    description='pYthon-based REST api to manage | sort | stream | backup media files',
    long_description=file('README.md').read(),
    author='Robert Schumann',
    author_email='rs@n-os.org',
    maintainer='Robert Schumann',
    maintainer_email='rs@n-os.org',
    license=file('LICENSE').read(),
    url='http://n-os.org/bynge/',
    platforms='any',

    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License'
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    # Read package data files from MANIFEST.in
    # (no need for a package_data directive).
    include_package_data=True,

    # Automatically find Python packages.
    packages=find_packages(),

    # Do not allow to be installed as zip archive.
    zip_safe=False,

    # Required packages.
    # See http://justcramer.com/2012/04/24/sticking-with-standards/
    install_requires=[line.strip() for line in file('requirements.txt')],

    # Look for own packages here. Simply an http directory listing of correctly
    # named tarballs.
    ## dependency_links=['http://...']
)