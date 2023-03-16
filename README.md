Python script that reads an `.ods` (libreoffice calc) with an author list and transform it to `.tex` in the following format:

```tex
\author{} 
\affiliation{} 
```

A typical ODS spreadsheet file might look like this:

| First      | First Abb. | Last  | Email               | ORCID               | 1. Afiiliation  | 2. Affiliation  | 3. Affiliation |
|------------|------------|-------|---------------------|---------------------|-----------------|-----------------|----------------|
| Eva Lilith | E. L.      | Cielo | elcielo@example.edu | 0000-0123-4567-8910 | City University | College of Arts |                |


## Installation
Clone this repository with:
```bash
    git clone https://github.com/DFreireF/collodstex.git
```
Then use `pip` for installing `collodstex`.

```bash
  pip install -r requirements.txt
  pip install .
```

## Usage

Run it as a python module

    python -m collodstex /your/path/with/thefile.ods

Or once installed, you can use from anywhere with:

    collodstex /your/path/with/thefile.ods

Then it will create a `thefile.tex` at `/your/path/with/thefile.tex` with authors and affiliations. Output file name can be changed by `--texout` option.
