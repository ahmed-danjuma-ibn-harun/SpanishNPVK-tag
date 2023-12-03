from setuptools import setup

setup(
    name='spanishnpvk',
    version='0.1',
    description='A module for extracting Nouns, Proper Nouns, Verbs, and Keywords in Spanish.',
    py_modules=['spanishnpvk'],
    install_requires=[
        'spacy',
        'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

