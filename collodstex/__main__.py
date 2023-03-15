import ezodf
import argparse
import os
import logging as log

def main():
    
    scriptname = 'odsTOlatex-authorlist' 
    parser = argparse.ArgumentParser()

    # Main Arguments
    parser.add_argument('odsin', type = str, nargs = '+', help = 'Name of the ods.')
    parser.add_argument('texout', type = str, nargs = '?', help = 'Name of the tex.')

    # Actions
    parser.add_argument('-l', '--log', dest = 'logLevel', choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default = 'INFO', help = 'Set the logging level.')
    parser.add_argument('-o', '--outdir', type = str, nargs = '?', default = os.getcwd(), help = 'Output directory.')

    args = parser.parse_args()

    # Checking for Argument Errors
    if args.texout is None:
        parser.error('Please introduce the revolution frequency of the reference nucleus or the brho parameter or ke/aa or gamma.')

    # Extra Details
    if args.logLevel: log.basicConfig(level = log.getLevelName(args.logLevel))
    if args.outdir: outfilepath = os.path.join(args.outdir, '')
        
    
    # Here We Go:
    print(f'Running {scriptname}... Lets see what we have in our ring ;-)')
    log.info(f'File {args.datafile} passed for creating latex author list as {args.refion}.')

    controller(args.odsin, args.texout)
    
def controller(odsin, textout = None):
    
    try:
        with open(odsin, 'r') as f:
            pass
    except FileNotFoundError:
        print(f'File not found: {odsin}')
    except PermissionError:
        print(f'Permission denied: cannot read {odsin}')
    except Exception as e:
        print('Error reading file:', e)
        
    # Open the .ods file    
    odsinfo = ezodf.opendoc(odsin)
    # Get the first sheet
    sheet = odsinfo.sheets[0]

    alla = []
    for row in range(1, sheet.nrows()):
        affiliations = []
        afil_str = ''

        # Loop through the columns in the row
        for col in range(1, sheet.ncols()):
            # Get the cell value
            cell = sheet[row, col].value
            
            if col == 1:
                authors1 = cell
            elif col == 2:
                authors2 = cell
                
            elif col ==3: continue #emails
            elif col == 4: continue #ORCID
            else:
                affiliations.append(cell)
        for af in affiliations:
            if af is not None:
                afil_str = afil_str + '\\affiliation{'+af+'}\n'
                
        author_str = authors1 +' '+ authors2
        names = '\\author{'+author_str+'}\n'
        alla.append(names+afil_str)
        
    if textout is None: 
        head, tail = os.path.split(odsin)
        textout = head + '/' + tail[:-4] + '.tex'
    with open(textout, 'w') as f:
        for row in alla:
            f.write(row)

if __name__ == '__main__':
    main()