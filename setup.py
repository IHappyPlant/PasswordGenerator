# coding=utf-8
"""
This module contains code for deploying Password generator application
"""
from setuptools import setup

required_packages = ['pyqt5']

setup(
    name='password_generator',
    version='1.0',
    url='https://github.com/IHappyPlant/PasswordGeneratorGui',
    author='IHappyPlant',
    author_email='karuk1998@yandex.ru',
    license='MIT',
    description='GUI app to generating passwords',
    packages=['password_generator'],
    install_requires=required_packages,
    include_package_data=True,
    python_requires='>=3.6',
    keywords="password generator password-generator python3 gui application "
             "app",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
        'Topic :: Security',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Natural Language :: English',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education'
    ]
)
