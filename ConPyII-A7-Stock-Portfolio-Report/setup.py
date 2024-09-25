"""
Installs the program with requirements
"""
from setuptools import setup, find_packages

setup(
    name='portfolio_report',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'certifi',
        'charset-normalizer',
        'idna',
        'requests',
        'requests-mock',
        'six',
        'urllib3',
        'python-dotenv',
        'pytest',
        'pylint',
    ],
    entry_points={
        'console_scripts': [
            'portfolio_report=portfolio.portfolio_report:main',
        ],
    },
)
