import csv
import math
import numpy as np
import pickle
import sys

times = [0, 9.5, 11.5, 13.5, 15.5, 18.5, 20.5] # Hours


def extrapolate_first(y0, y1):
    x = times[0]
    x0 = times[1]
    x1 = times[2]
    y = y0 - (y1 - y0) / (x1 - x0) * (x0 - x)
    return y


def interpolate(missing_index, y0, y1):
    x = times[missing_index]
    x0 = times[missing_index - 1]
    x1 = times[missing_index + 1]
    y = ((y0 * (x1 - x)) + (y1 * (x - x0))) / (x1 - x0)
    return y


def extrapolate_last(y0, y1):
    x = times[-1]
    x0 = times[-3]
    x1 = times[-2]
    y = y0 + (x - x0) / (x1 - x0) * (y1 - y0)
    return y


def log_fold_change(this_pt, first_pt):
    return math.log2(this_pt / first_pt)


def main():
    if len(sys.argv) != 3:
        sys.exit(f'Usage: python3 {sys.argv[0]} <data-file> <output-file>')

    matrix = []
    with open(sys.argv[1], 'rt') as file:
        next(file) # Skip first line
        tsv_file = csv.reader(file, delimiter='\t')
    
        for line in tsv_file:
            line = line[1:] # Skip first value of every line
            
            # Skip samples with more than 2 missing values in a row
            skip_line = False
            prev_missing_value = False
            for value in line:
                if value == 'NA':
                    if prev_missing_value:
                        skip_line = True
                    else:
                        prev_missing_value = True
                else:
                    prev_missing_value = False
            if skip_line:
                continue

            for i in range(len(line)):
                if i == 0 or i == len(line) - 1: # Skip first and last value
                    continue
                if line[i] == 'NA': # Interpolate missing middle values
                    line[i] = interpolate(i, float(line[i - 1]), float(line[i + 1]))
                else:
                    line[i] = float(line[i])

            # Extrapolate first value if missing            
            if line[0] == 'NA':
                line[0] = extrapolate_first(float(line[1]), float(line[2]))
            else:
                line[0] = float(line[0])

            # Extrapolate last value if missing            
            if line[-1] == 'NA':
                line[-1] = extrapolate_last(float(line[-3]), float(line[-2]))
            else:
                line[-1] = float(line[-1])

            matrix.append(line)

    # Normalize
    for row in matrix:
        for i in range(len(row)):
            try:
                row[i] = log_fold_change(row[i], row[0])
            except: # Handle division by zero
                break

    # Save preprocessed data
    with open(sys.argv[2], 'wb') as file:
        pickle.dump(matrix, file)
        

if __name__ == '__main__':
    main()

