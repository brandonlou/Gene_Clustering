import csv
import math
import numpy as np
import pandas as pd
import pickle
import sys

times = [0, 9.5, 11.5, 13.5, 15.5, 18.5, 20.5] # Hours


def main():
    if len(sys.argv) != 3:
        sys.exit(f'Usage: python3 {sys.argv[0]} <data-file> <output-file>')

    matrix = []

    with open(sys.argv[1], 'rt') as file:
        next(file) # Skip first line
        tsv_file = csv.reader(file, delimiter='\t')
    
        for line in tsv_file:
            line = line[1:] # Skip first value of every line
            # Convert values from strings to floats (and NaN)
            for i in range(len(line)):
                if line[i] == 'NA':
                    line[i] = np.nan
                else:
                    line[i] = float(line[i])
            line = pd.Series(data=line, index=times)
            
            # Interpolate and extrapolate missing values
            try:
                line = line.interpolate(method='slinear', fill_value='extrapolate', limit_direction='both')
            except:
                print(f'Removing {line.values}')
                continue
        
            # Skip any data points with NaN
            if True in np.isnan(line.values):
                print(f'Removing {line.values}')
                continue

            matrix.append(line.values)

    """    
    for i in range(len(matrix)):
        matrix[i] = matrix[i] + 1            # Add constant to every number to avoid dividing by 0
        matrix[i] = matrix[i] / matrix[i][0] # Normalize to first data point
        matrix[i] = matrix[i].tolist()
    """

    # Save preprocessed data
    with open(sys.argv[2], 'wb') as file:
        pickle.dump(matrix, file)

    print('Done.')
        

if __name__ == '__main__':
    main()

