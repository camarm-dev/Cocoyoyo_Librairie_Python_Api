from setuptools import setup, find_packages

VERSION = '1.5.0'
DESCRIPTION = 'Official CocoyoyoLibrairie API packages'
LONG_DESCRIPTION = 'A package to search books and users on the cocoyoyolibrairie !'

setup(
    name="cocoyoyo_librairie_api",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="CAMARM-DEV",
    author_email="armand@camponovo.xyz",
    license='MIT',
    packages=['cocoyoyo_librairie_api'],
    install_requires=['requests~=2.25.1',
                      'colorama~=0.4.4',
                      ],
    keywords='conversion',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
