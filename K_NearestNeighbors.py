import heapq


def k_nearest(points, n):

    class Point:
        def __init__(self, point):
            self.point = point
            self.distance = -1 * (point[0] ** 2 + point[1] ** 2) ** (1 / 2)

        def __lt__(self, other):
            return self.distance < other.distance

    heap = [Point((float('-inf'), float('-inf')))] * n
    heapq.heapify(heap)

    for p in [Point(point) for point in points]:
        heapq.heappushpop(heap, p)

    return [point.point for point in heap]


if __name__ == '__main__':
    p = [
        (-5, 2),
        (-1, 1),
        (0, 1),
        (1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (-2, -2)
    ]

    nearest = k_nearest(p, 3)
    for point in nearest:
        print(point)
