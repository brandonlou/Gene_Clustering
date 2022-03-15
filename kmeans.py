import copy
import math
import pickle
import random
import sys

NUM_CLUSTERS = 2
MAX_ITER = 500
THRESHOLD = 0.01


def get_min_max(matrix):
    min_element = matrix[0][0]
    max_element = matrix[0][0]
    for row in matrix:
        for element in row:
            min_element = min(element, min_element)
            max_element = max(element, max_element)
    return min_element, max_element


def random_point(min_val, max_val, dim):
    point = []
    for _ in range(dim):
        num = random.uniform(min_val, max_val)
        point.append(num)
    return point


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


def get_wss(clusters):
    wss = 0
    for cluster in clusters:
        dist_sum = 0
        for point1 in cluster:
            for point2 in cluster:
                dist_sum += math.dist(point1, point2)
        normalized_sum = dist_sum / (2 * len(cluster))
        wss += normalized_sum

    return wss


def main():
    if len(sys.argv) != 3:
        sys.exit(f'Usage: python3 {sys.argv[0]} <data-pkl> <output-pkl>')

    with open(sys.argv[1], 'rb') as file:
        data = pickle.load(file)

    min_element, max_element = get_min_max(data)
    dim = len(data[0])

    # Initialize centers
    centers = []
    cog = get_cog(data)
    for _ in range(NUM_CLUSTERS):
        pt = copy.copy(cog)
        for i in range(dim):
            pt[i] += random.uniform(-0.1, 0.1)
        centers.append(pt)
    
    for i in range(MAX_ITER):
        clusters = e_step(data, centers)
        centers = m_step(clusters)
        #if diff < THRESHOLD:
        #     break
        #prev_wss = wss
    
    with open(sys.argv[2], 'wb') as file:
        pickle.dump(clusters, file)

    print(f'k = {NUM_CLUSTERS}')
    print(f'wss = {get_wss(clusters)}')


if __name__ == '__main__':
    main()

