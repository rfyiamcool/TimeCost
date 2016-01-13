import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "timecost",
        version = "1.5",
        author = "ruifengyun",
        author_email = "rfyiamcool@163.com",
        description = "task cost time",
        license = "MIT",
        keywords = ["task cost time","fengyun"],
        url = "https://github.com/rfyiamcool",
        long_description = read('README.md'),
        scripts = ['timecost.py'],
        classifiers = [
             'Development Status :: 2 - Pre-Alpha',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: MIT License',
             'Programming Language :: Python :: 2.7',
             'Programming Language :: Python :: 3.0',
             'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)

