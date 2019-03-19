from setuptools import setup, find_packages

setup(
    name='sortpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA recursion and sorting package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/RobTheDay/sortpackage',
    author='Rob Fairon',
    author_email='rmfairon.ds@gmail.com'
)
