from setuptools import setup

setup(
    name='pytest-pythonpath',
    description='pytest plugin for adding to the PYTHONPATH from command line or configs.',
    long_description=open("README.md").read(),
    version='0.1',
    author='Eric Palakovich Carr',
    author_email='carreric@gmail.com',
    url='https://github.com/bigsassy/pytest-pythonpath',
    py_modules=['pytest_pythonpath'],
    entry_points={'pytest11': ['pythonpath = pytest_pythonpath']},
    install_requires=['pytest>=2.5.2']
)
