from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Portfolio Analysis'
long_description = 'This package allows you to compute the standard deviation of a portfolio, \n' \
                   'whatever it is the number of stocks are in it, or the correlation table.\n' \
                    '------------------------------------------------------------------------------------------------------\n' \
                    "The algorithm for the standard deviation of the portfolio follow this formula \nand it's based on the returns of the stocks:\n" \
                                        "σ² = Σ°Σ'[w°w'σ(R°,R')]\n"


# Setting up
setup(
    name="Bruni",
    version=VERSION,
    author="Federico Bruni",
    author_email="brunifederico99@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pandas', 'pandas-datareader', 'numpy','datetime'],
    keywords=['python', 'portfolio', 'standard deviation', 'std', 'stocks','Bruni'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: MacOS :: MacOS X"

    ]
)