import os
from pip.download import PipSession
from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt', session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name='hodorlive',
    version='1.0',
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    license='MIT',
    description='xpath/css based scraper with pagination',
    keywords = ['hodor', 'cssselect', 'lxml', 'scraping'],
    url='https://github.com/CompileInc/hodor',
    download_url = 'https://github.com/CompileInc/hodor/archive/v1.0.tar.gz',
    author='Compile Inc',
    author_email='dev@compile.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
