#一定要导入本地的ECFP6

import pandas as pd
from molvs import standardize_smiles
from ECFP6 import *

def main():
    filename = 'smiles.csv'  # path to your csv file
    df = pd.read_csv(filename)               # read the csv file as pandas data frame
    smiles = [standardize_smiles(i) for i in df['smiles'].values]  

    ## Compute ECFP6 Fingerprints and export a csv file.
    ecfp6_descriptor = ECFP6(smiles)        # create your ECFP6 object and provide smiles
    ecfp6_descriptor.compute_ECFP6(filename) # compute ECFP6 and provide the name of your desired output file. you can use the same name as the input file because the ECFP6 class will ensure to add "_ECFP6.csv" as part of the output file.

if __name__ == '__main__':
    main()