from setuptools import setup, find_packages

print(find_packages())
__version__ = "0.1"

setup(
    name='amrsy_log',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    zip_safe=True,
    python_requires='>=3.6',
    install_requires=[
        'psutil',
    ],
)