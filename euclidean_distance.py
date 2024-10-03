import math

def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def main():
    points = []
    distances = []
    
    while True:
        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))
        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))

        point1 = (x1, y1)
        point2 = (x2, y2)
        points.append(point1)
        points.append(point2)

        distance = euclideanDistance(point1, point2)
        distances.append(distance)
        print(f"Euclidean distance between {point1} and {point2}: {distance:.2f}")

        cont = input("Do you want to enter another set of points? (y/n): ").lower()
        if cont == 'n':
            break

    if distances:
        min_distance = min(distances)
        print(f"Minimum Euclidean distance between all points is: {min_distance:.2f}")
    else:
        print("No distances were calculated.")

main()
