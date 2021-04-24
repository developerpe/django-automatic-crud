import os
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='django-automatic-crud',
    version='1.2.0',
    packages=['automatic_crud'],
    include_package_data=True,
    license='BSD License',
    description='CRUDS Automáticos con Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/developerpe/django-automatic-crud',
    author='Oliver Sandoval',
    author_email='developerpeperu@gmail.com',
    install_requires=[
        'Django>=2.2',
        'openpyxl==3.0.7',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3'
    ]
)