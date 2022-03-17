import pickle
import sys
from sklearn.mixture import GaussianMixture
from kmeans import get_wss

NUM_CLUSTERS = 7


def main():
    if len(sys.argv) != 3:
        sys.exit(f'Usage: python3 {sys.argv[0]} <data-pkl> <clusters-pkl>')

    with open(sys.argv[1], 'rb') as file:
        data = pickle.load(file)

    gm = GaussianMixture(n_components=NUM_CLUSTERS)
    labels = gm.fit_predict(data)

    clusters = []
    for _ in range(NUM_CLUSTERS):
        clusters.append([])

    for i, label in enumerate(labels):
        clusters[label].append(data[i])

    #wss = get_wss(clusters)
    #print(f'k = {NUM_CLUSTERS}, W_k = {wss}')

    with open(sys.argv[2], 'wb') as file:
        pickle.dump(clusters, file)


if __name__ == '__main__':
    main()

