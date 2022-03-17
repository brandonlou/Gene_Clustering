import matplotlib.pyplot as plt
import numpy as np
import pickle
import scipy.stats
from gap_statistic import OptimalK
from sklearn.mixture import GaussianMixture

plt.rcParams['font.family'] = 'Times New Roman'


def GMM(X, k):
    gm = GaussianMixture(n_components=k).fit(X)

    # https://stackoverflow.com/questions/47412749/how-can-i-get-a-representative-point-of-a-gmm-cluster
    centers = np.empty(shape=(gm.n_components, X.shape[1]))
    for i in range(gm.n_components):
        density = scipy.stats.multivariate_normal(cov=gm.covariances_[i], mean=gm.means_[i]).logpdf(X)
        centers[i, :] = X[np.argmax(density)]

    labels = gm.predict(X)

    return centers, labels


def main():
    with open('data.pkl', 'rb') as file:
        X = pickle.load(file)
    X = np.array(X)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    optimalK = OptimalK()
    optimalK(X, cluster_array=np.arange(1, 11))
    ax[0].set_title('k-means')
    ax[0].set_xlabel(r'$k$')
    ax[0].set_ylabel('Gap value')
    ax[0].plot(optimalK.gap_df.n_clusters, optimalK.gap_df.gap_value)

    optimalK = OptimalK(clusterer=GMM)
    optimalK(X, cluster_array=np.arange(1, 11))
    ax[1].set_title('GMM')
    ax[1].set_xlabel(r'$k$')
    ax[1].set_ylabel('Gap value')
    ax[1].plot(optimalK.gap_df.n_clusters, optimalK.gap_df.gap_value)
    
    plt.savefig('gap.png', dpi=300, bbox_inches='tight')

    plt.show()

if __name__ == '__main__':
    main()

