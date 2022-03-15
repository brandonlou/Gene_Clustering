import matplotlib.pyplot as plt


def main():
    k = (1, 2, 3, 4, 5, 6, 7)
    wss = (5956.2354725799605, 4804.485392963301, 4330.186781351326, 3997.740170293275, 3897.07441145757, 3758.674280495394, 3652.6073247603126)

    plt.plot(k, wss)
    plt.title('Within sum of squares per number of clusters')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Within sum of squares (Wk)')
    plt.show()


if __name__ == '__main__':
    main()

