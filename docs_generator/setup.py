from setuptools import setup, find_packages
from datetime import datetime

now = datetime.now()
setup(
    name='docs_generator',
    version=f'{now.year}-{now.month}-{now.day}-{now.hour}',
    install_requires=[
        'jupyter',
        'mkdocs',
        'pyyaml',
        'mkdocs-material',
        'pytest'
    ],
    packages=['docs_generator'],
    url='https://github.com/sirily11/algorithms',
    license='',
    author='sirily11',
    author_email='sirily1997@gmail.com',
    description='A program which convert jupyter notebook to mkdocs'
)
