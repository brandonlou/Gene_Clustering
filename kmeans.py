import copy
import math
import pickle
import random
import sys

NUM_CLUSTERS = 7
MAX_ITER = 300
MAX_ATTEMPTS = 10
THRESHOLD = 0.0001


# Compute center of gravity
def get_cog(points):
    num_points = len(points)
    dim = len(points[0])
    cog = [0] * dim
    for point in points:
        for i in range(len(point)):
            cog[i] += point[i]
    for i in range(len(cog)):
        cog[i] /= num_points
    return cog


# Assign data points to the nearest center
def e_step(data, centers):
    clusters = []
    for _ in range(NUM_CLUSTERS):
        clusters.append([])
    for point in data:
        distances = []
        for center in centers:
            dist_to_center = math.dist(point, center)
            distances.append(dist_to_center)
        i = distances.index(min(distances))
        clusters[i].append(point)

    return clusters


# Compute new centers
def m_step(clusters):
    new_centers = []
    for cluster in clusters:
        cog = get_cog(cluster)
        new_centers.append(cog)
    return new_centers


def get_squared_error_distortion(centers, clusters):
    n = 0
    total = 0
    for i, cluster in enumerate(clusters):
        n += len(clusters)
        for point in cluster:
            total += math.dist(point, centers[i])**2
    total /= n
    return total


# Compute within sum of squares given a list of clusters
def get_wss(clusters):
    wss = 0
    for cluster in clusters:
        dist_sum = 0
        for i in range(len(cluster) - 1):
            for j in range(i + 1, len(cluster)):
                dist_sum += math.dist(cluster[i], cluster[j])
        normalized_sum = dist_sum / len(cluster)
        wss += normalized_sum
    return wss


def main():
    if len(sys.argv) != 3:
        sys.exit(f'Usage: python3 {sys.argv[0]} <data-pkl> <output-pkl>')

    with open(sys.argv[1], 'rb') as file:
        data = pickle.load(file)

    best_clusters = None
    smallest_distortion = sys.maxsize

    # Run k-means a given number of times and keep the best clusters
    for attempt_num in range(MAX_ATTEMPTS):
        prev_distortion = sys.maxsize

        # Initialize centers by choosing random data points
        centers = set()
        while len(centers) < NUM_CLUSTERS:
            i = random.randint(0, len(data) - 1)
            centers.add(tuple(data[i]))
        centers = list(centers)
        
        # Run the e and m step up to a maximum number of times
        for iter_num in range(MAX_ITER):
            clusters = e_step(data, centers)
            centers = m_step(clusters)
            distortion = get_squared_error_distortion(centers, clusters)

            print(f'Attempt: {attempt_num + 1}, Iteration: {iter_num + 1}, distortion = {distortion}')

            # If the difference between distortions is lower than a threshold, k-means has converged
            if abs(distortion - prev_distortion) < THRESHOLD:
                prev_distortion = distortion
                break
            else:
                prev_distortion = distortion

        # If this instance of clustering is better, save it
        if prev_distortion < smallest_distortion:
            smallest_distortion = prev_distortion
            best_clusters = clusters

    print('Data:', len(data))
    for i in range(len(best_clusters)):
        print(f'Cluster {i}: {len(best_clusters[i])}')

    with open(sys.argv[2], 'wb') as file:
        pickle.dump(best_clusters, file)

    wss = get_wss(best_clusters)
    print(f'k = {NUM_CLUSTERS}, W_k = {wss}')


if __name__ == '__main__':
    main()

