"""
How to upload
python setup.py clean sdist bdist_wheel
twine upload dist/*
"""


# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md')) as fd:
    md = fd.read()


setup(
    name='pycond',
    version='20190415',
    description='Lightweight condition parsing and building of evaluation expressions',
    long_description=md,
    long_description_content_type='text/markdown',
    install_requires=[],
    include_package_data=True,
    url='https://github.com/axiros/pycond',
    author='gk',
    author_email='gk@axiros.com',
    license='BSD',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Text Editors :: Text Processing',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords=[
        'conditions',
        'expression',
        'serialization',
        'rxpy',
        'reactivex',
    ],
    py_modules=['pycond'],
    entry_points={},
    zip_safe=False,
)
