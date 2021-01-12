from setuptools import setup

INSTALL_REQUIRES = [
    'numpy'
]
TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',
    # unmandatory dependencies of the package itself
    'pandas', 'lime',
    # to be able to run `python setup.py checkdocs`
    'collective.checkdocs', 'pygments',
]

setup(
    name='CTCI',
    author='Victor Cannestro',
    description='Solutions to problems from the 6th edition of Cracking the Coding Interview',
    long_description=README,
    url='https://github.com/VictorCannestro/ctci',
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
    }
)
