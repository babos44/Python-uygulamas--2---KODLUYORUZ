# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:44:59 2024

@author: ASUS
"""
#Kodluyoruz-Python Uygulaması 2 - Minimum Öklid Mesafesi Hesaplama 
import math

def get_points():
    points = []
    n = int(input("Kaç tane nokta gireceksiniz? "))
    for i in range(n):
        x = float(input("{}. noktanın x koordinatını girin: ".format(i+1)))
        y = float(input("{}. noktanın y koordinatını girin: ".format(i+1)))
        points.append((x, y))
    return points

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def calculate_distances(points):
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)
    return distances


def find_min_distance(distances):
    min_distance = min(distances)
    return min_distance


points = get_points()

distances = calculate_distances(points)

min_distance = find_min_distance(distances)

print("Minimum Mesafe:", min_distance)
