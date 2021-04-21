import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__fila__), os.pardir)))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()


setup(
    name='django-automatic-crud',
    version='1.0',
    packages=['automatic_crud'],
    include_package_data=True,
    license='BSD License',
    description='CRUDS Automáticos con Django',
    url='https://github.com/developerpe/django-automatic-crud',
    author='Oliver Sandoval',
    author_email='developerpeperu@gmail.com',
    long_description=read('README.md'),
    install_required=[
        'asgiref==3.3.1',
        'Django==3.1.7',
        'et-xmlfile==1.0.1',
        'openpyxl==3.0.7',
        'pytz==2021.1',
        'sqlparse==0.4.1'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intented Audience :: Developers',
        'License :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3'
    ]
)