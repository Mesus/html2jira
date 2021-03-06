# coding: utf-8
import sys
from setuptools import setup, find_packages, Command

requires_list = []
try:
    import unittest2 as unittest
except ImportError:
    import unittest
else:
    if sys.version_info <= (2, 6):
        requires_list.append("unittest2")


class RunTests(Command):
    """New setup.py command to run all tests for the package.
    """
    description = "run all tests for the package"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        tests = unittest.TestLoader().discover('.')
        runner = unittest.TextTestRunner()
        runner.run(tests)


setup(
    name="html2jira",
    version="2014.4.5",
    description="Turn HTML into equivalent Markdown-structured text.",
    author="Aaron Swartz",
    author_email="me@aaronsw.com",
    maintainer='Ian Wallis',
    maintainer_email='Qazzian@gmail.com',
    url='https://github.com/Qazzian/html2jira/',
    cmdclass={'test': RunTests},
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
    ],
    entry_points="""
        [console_scripts]
        html2jira=html2jira:main
    """,
    license='GNU GPL 3',
    requires=requires_list,
    packages=find_packages(),
    py_modules=['html2jira'],
    include_package_data=True,
    zip_safe=False,
)
