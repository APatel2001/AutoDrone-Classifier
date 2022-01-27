import cv2
import numpy as np

def avg_intensity(img, color) -> int:
    b,g,r = cv2.split(img)
    avg = 0
    pixels = 0
    
    if color == "red":
        for i in range(len(r)):
            for j in range(len(r[i])):
                redness = max(0, int(r[i][j]) - (int(b[i][j]) + int(g[i][j])) / 2)
                avg += redness
                pixels += 1
    elif color == "green":
        for i in range(len(g)):
            for j in range (len(g[i])):
                greenness = max(0, int(g[i][j]) - (int(b[i][j]) + int(r[i][j])) / 2)
                avg += greenness
                pixels += 1
    elif color == "blue":
        for i in range(len(b)):
            for j in range (len(b[i])):
                blueness = max(0, int(b[i][j]) - (int(g[i][j]) + int(r[i][j])) / 2)
                avg += blueness
                pixels += 1
    avg /= pixels
    return avg

green_light = cv2.imread("green_light_dectection.png")
lights_off = cv2.imread("lights_off_dectection.png")



print(f'\n\n\nAverage Intensity for Green: {avg_intensity(lights_off, "green")}\n\n\n')
print(f'Lights Off ------ red: {avg_intensity(lights_off, "red")} blue: {avg_intensity(lights_off, "blue")} green: {avg_intensity(lights_off, "green")}')

