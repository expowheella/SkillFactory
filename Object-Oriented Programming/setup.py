from setuptools import find_packages, setup

setup(
    name="mylibrary",
    packages=find_packages(include="mylibrary"),
    version='0.0.1',
    description="My Python library",
    author="Bulat",
    license="MIT",
    install_requires=[],
    setup_requires=['pytest-runner'],
    test_require=['pytest==4.4.1'],
    test_suite='tests',
)
