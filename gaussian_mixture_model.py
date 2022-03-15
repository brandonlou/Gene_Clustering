import pickle
import sys
from sklearn.mixture import GaussianMixture

NUM_CLUSTERS = 2


def main():
    if len(sys.argv) != 2:
        sys.exit(f'Usage: python3 {sys.argv[0]} <data-file>')

    with open(sys.argv[1], 'rb') as file:
        data = pickle.load(file)

    gm = GaussianMixture(n_components=NUM_CLUSTERS)
    labels = gm.fit_predict(data)

    clusters = []
    for _ in range(NUM_CLUSTERS):
        clusters.append([])

    for i, label in enumerate(labels):
        clusters[label].append(data[i])

    with open('clusters.pkl', 'wb') as file:
        pickle.dump(clusters, file)


if __name__ == '__main__':
    main()

