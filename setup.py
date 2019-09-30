from setuptools import setup

with open('README.rst', 'r') as readme_file:
    readme_txt = readme_file.read()

setup(
    name='simple-specification',
    packages=['simple_specification'],
    version='0.1',
    description='A simple pythonic implementation of the Specification Pattern for Python 3.7 or higher.',
    long_description=readme_txt,
    long_description_content_type='text/x-rst',
    author='Victor Oliveira da Silva',
    author_email='victor_o_silva@hotmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    url='https://github.com/victor-o-silva/simple-specification',
    download_url='https://github.com/victor-o-silva/simple-specification/tarball/0.1'
)
