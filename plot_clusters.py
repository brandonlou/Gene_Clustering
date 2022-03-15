import matplotlib.pyplot as plt
import pickle
import sys

x_data = [0, 9.5, 11.5, 13.5, 15.5, 18.5, 20.5]

# TODO: Separate plots? Or all in one go
def main():
    if len(sys.argv) != 2:
        sys.exit(f'Usage: python3 {sys.argv[0]} <clusters-file>')

    with open(sys.argv[1], 'rb') as file:
        clusters = pickle.load(file)

    num_clusters = len(clusters)
    cmap = plt.cm.get_cmap('hsv', num_clusters + 1)

    for i, cluster in enumerate(clusters):
        for y_data in cluster:
            plt.subplot(num_clusters, 1, i + 1)
            plt.plot(x_data, y_data, c=cmap(i))
            plt.title(f'Cluster {i + 1}')

    plt.suptitle('Gene expression levels over time')
    #plt.xlabel('Time (hours)')
    #plt.ylabel('Expression Level')
    plt.show()


if __name__ == '__main__':
    main()

