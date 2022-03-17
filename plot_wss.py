import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Times New Roman'

def main():
    X = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    y = (6409.5050165738585, 5206.139760702394, 4702.203792571841, 4355.901991124691, 4275.461523094639, 4079.431558964134, 4017.415139913008, 3862.7158323898607, 3760.4497896030903, 3665.8979090455946)
    ax[0].set_title('k-means')
    ax[0].set_xlabel(r'$k$')
    ax[0].set_ylabel(r'$W_k$')
    ax[0].plot(X, y)

    y = (6409.5050165738585, 6238.567073930677, 6096.261615244299, 5984.2276151015485, 5875.150743220539, 5671.87525373433, 5536.4121747499385, 5176.37257856144, 4813.558224982838, 4736.579104079028)
    ax[1].set_title('GMM')
    ax[1].plot(X, y)
    ax[1].set_xlabel(r'$k$')
    ax[1].set_ylabel(r'$W_k$')

    plt.savefig('wss.png', dpi=300, bbox_inches='tight')

    plt.show()

if __name__ == '__main__':
    main()

