import sys
import math

def circle_data(file_path):
    with open(file_path, 'r') as f:
        c_x, c_y = map(float, f.readline().strip().split())
        radius = float(f.readline().strip())
    return c_x, c_y, radius

def points_data(file_path):
    with open(file_path, 'r') as f:
        points = []
        for line in f:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

def calculate_position(c_x, c_y, radius, point_x, point_y):
   
    distance = math.sqrt((point_x - c_x) ** 2 + (point_y - c_y) ** 2)
    if distance < radius:
        return 1 
    elif distance == radius:
        return 0 
    else:
        return 2

if __name__ == "__main__":
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    c_x, c_y, radius = circle_data(circle_file)
    points = points_data(points_file)

    for point_x, point_y in points:
        position = calculate_position(c_x, c_y, radius, point_x, point_y)
        print(position)
