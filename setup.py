from setuptools import setup, find_packages
from collodstex.version import __version__
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

classifiers = [
    'Environment :: Console',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Topic :: Text Processing :: Markup :: LaTeX'

]

setup(
    name='collodstex',
    packages=find_packages(),
    version=__version__,
    description='...',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='DFreireF',
    url='https://github.com/DFreireF/collodstex',
    download_url=f'https://github.com/DFreireF/collodstex/tarball/{__version__}',
    entry_points={
        'console_scripts': [
            'collodstex = collodstex.__main__:main'
        ]
    },
    license='GPLv3',
    keywords=['collaboration list', 'author', 'affiliation', ],
    classifiers=classifiers
)
