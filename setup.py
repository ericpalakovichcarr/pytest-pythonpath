from setuptools import setup

description = 'pytest plugin for adding to the PYTHONPATH from command line or configs.'
try:
    long_description = open("README.md").read()
except:
    long_description = description

setup(
    name='pytest-pythonpath',
    description=description,
    long_description=long_description,
    license='MIT',
    version='0.7.2',
    author='Eric Palakovich Carr',
    author_email='carreric@gmail.com',
    url='https://github.com/bigsassy/pytest-pythonpath',
    py_modules=['pytest_pythonpath'],
    entry_points={'pytest11': ['pythonpath = pytest_pythonpath']},
    install_requires=['pytest>=2.5.2'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Testing",
    ],
)
