# Gene Clustering

## Usage
0. Install Python 3.9.9. Install `numpy`, `pandas`, `matplotlib`, `scipy`, `sklearn`, and `gap-stat`
1. Preprocess the data by running `python3 preprocess.py yeast.tsv data.pkl`
2. Cluster using k-means by running `python3 kmeans.py data.pkl clusters.pkl` \
    a. Change k in `kmeans.py`
3. Cluster using Gaussian mixture model by running `python3 gmm.py data.pkl clusters.pkl` \
    a. Change k in `gmm.py`
4. Plot within sum of squares by running `python3 plot_wss.py`\
    a. Change wss values in `plot_wss.py`
5. Plot gap statistic by running `python3 python3 gap.py`
6. Plot clusters by running `python3 plot_clusters.py` \
    a. Change the filenames of the clusters in `plot_clusters.py`
