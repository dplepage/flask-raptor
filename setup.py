"""
Flask-Raptor
--------------

Flask support for the raptorize middleware.

Links
`````

* `documentation <http://packages.python.org/Flask-Raptor>`_


"""
from setuptools import setup


setup(
    name='Flask-Raptor',
    version='0.1',
    url='http://github.com/dplepage/flask-raptor',
    license='BSD',
    author='Dan Lepage',
    author_email='dplepage@gmail.com',
    maintainer='Dan Lepage',
    maintainer_email='dplepage@gmail.com',
    description='Raptor support for Flask',
    long_description=__doc__,
    packages=['flask_raptor'],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'raptorizemw',
    ],
    tests_require=[
        'nose',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
