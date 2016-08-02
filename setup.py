import os
from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='hodor',
    version='1.0',
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    license='Compile Proprietary',
    description='xpath based scraper',
    long_description=README,
    url='http://www.compile.com/',
    author='Compile Engineering',
    author_email='dev@compile.com',
    cmdclass={
    },
    classifiers=[
        'Environment :: Backend',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
