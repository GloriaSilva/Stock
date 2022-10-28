from setuptools import setup, find_packages

setup(
    name='modules_price',
    version='1.0.0',
    description='This is a working setup.py',
    url='',
    author='Gloria Silva',
    author_email='g.silva@cheil.com',
    packages=find_packages(),
    install_requires=[
        'requests','pandas','pyyaml','bs4','sqlalchemy'
    ],
    zip_safe=False
)