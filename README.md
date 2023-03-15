Python script that reads an .ods (libreoffice calc) with an author list and transform it to .tex with:
\author{} 
\affiliation{} 
format

## Installation
Clone the repository or download the source from [GitHUB](https://github.com/DFreireF/collodstex.git). Then use `pip` for installing `collodstex`.

    pip install -r requirements.txt
That will install `collodstex`, `ezodf` and `lxml`

Once install, you can use from anywhere with:

python -m collodstex /your/path/with/thefile.ods

Then it will create a thefile.tex at /your/path/with/thefile.tex with authors and affiliations.


usage: __main__.py [-h] [-tex [TEXOUT]] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] odsin [odsin ...]

positional arguments:
  odsin                 Name of the ods.

options:
  -h, --help            show this help message and exit
  -tex [TEXOUT], --texout [TEXOUT]
                        Name of the tex.
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level.
                       
