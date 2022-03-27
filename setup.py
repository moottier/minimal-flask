from setuptools import setup, find_packages

setup(
    name='app', 
    description='My Flask Application',
    author='Andre Mottier',
    author_email='andre.mottier@gmail.com',
    version='1.0', 
    packages=find_packages(),
    license='Apache License 2.0',
    install_requires=[
        'flask',
        'flask-caching'
    ]
)