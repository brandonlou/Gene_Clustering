import matplotlib.pyplot as plt
import pickle
import sys
from kmeans import get_cog

plt.rcParams['font.family'] = 'Times New Roman'

X = [0, 9.5, 11.5, 13.5, 15.5, 18.5, 20.5]


def main():
    fig, ax = plt.subplots(1, 4, figsize=(15, 4))
    fig.tight_layout(pad=2)

    with open('cluster2_kmeans.pkl', 'rb') as file:
        clusters = pickle.load(file)
    cmap = plt.cm.get_cmap('hsv', len(clusters) + 1)
    for i in range(len(clusters)):
        y = get_cog(clusters[i])
        ax[0].plot(X, y, c=cmap(i))
    ax[0].set_title('k-means, k = 2')
    ax[0].set_xlabel('Time (hours)')
    ax[0].set_ylabel('Gene expression level')

    with open('cluster2_gmm.pkl', 'rb') as file:
        clusters = pickle.load(file)
    cmap = plt.cm.get_cmap('hsv', len(clusters) + 1)
    for i in range(len(clusters)):
        y = get_cog(clusters[i])
        ax[1].plot(X, y, c=cmap(i))
    ax[1].set_title('GMM, k = 2')
    ax[1].set_xlabel('Time (hours)')

    with open('cluster7_kmeans.pkl', 'rb') as file:
        clusters = pickle.load(file)
    cmap = plt.cm.get_cmap('hsv', len(clusters) + 1)
    for i in range(len(clusters)):
        y = get_cog(clusters[i])
        ax[2].plot(X, y, c=cmap(i))
    ax[2].set_title('k-means, k = 7')
    ax[2].set_xlabel('Time (hours)')

    with open('cluster7_gmm.pkl', 'rb') as file:
        clusters = pickle.load(file)
    cmap = plt.cm.get_cmap('hsv', len(clusters) + 1)
    for i in range(len(clusters)):
        y = get_cog(clusters[i])
        ax[3].plot(X, y, c=cmap(i))
    ax[3].set_title('GMM, k = 7')
    ax[3].set_xlabel('Time (hours)')
    
    fig.savefig('clusters.png', dpi=300, bbox_inches='tight')

    plt.show()


if __name__ == '__main__':
    main()

