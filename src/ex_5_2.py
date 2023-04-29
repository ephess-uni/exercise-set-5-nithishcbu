""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np
import os
try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":
    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"
    data = np.loadtxt(INFILE, delimiter=',')
#     data -= np.mean(data)
#     data /= np.std(data)
#     processed = data
#     # Save the output to OUTFILE using numpy routines.
#     np.savetxt(OUTFILE, processed, delimiter=',')

    centered = data - np.mean(data, axis=0)

    # TODO: scale the centered data by dividing each column by its standard deviation
    scaled = centered / np.std(centered, axis=0)
    os.makedirs(root_dir / "outputs", exist_ok=True)
    # TODO: save the processed data to a file
    np.savetxt(OUTFILE, scaled)


   
