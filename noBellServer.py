#!/usr/bin/env python3

import socket
import time
import json
import random
import subprocess
import serial
import cv2
import numpy as np
from ublox_gps import UbloxGps
vid = cv2.VideoCapture(0)
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65430  # Port to listen on (non-privileged ports are > 1023)
BASE_STATION_ADDRESS = "10.0.0.2"  # U-center NTRIP server address

# initiate NTRIP connection with base station
command = ["str2str", "-in", "ntrip://sae:1234@" +
           BASE_STATION_ADDRESS + ":2101/ARCT"]
serial_device = open['/dev/ttys0', 'w']
process = subprocess.Popen(
    command, stdout=serial_device, stderr=subprocess.PIPE, text=True)

# establish connection with GPS module stream
serial_port = serial.Serial('/dev/ttyS0', baudrate=38400, timeout=1)
gps = UbloxGps(serial_port)

TARGET_COLOR = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # initialize TCP Socket
    s.bind((HOST, PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.listen()
    print("Listening...")
    conn, addr = s.accept()  # spawn a sub-socket to deal with the client
    with conn:
        while True:
            request = conn.recv(1024).decode('utf-8')
            request_json = json.loads(request)

            match request_json["endpoint"]:
                case "target_color":
                    # Store target color
                    TARGET_COLOR = request_json["payload"]["color"]
                    #   Yeah, Well, I'm gonna go make my own AI!
                    while True:
                        ret, frame = vid.read()
                        cv2.imshow('frame', frame)
                        colorDetect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                        red_lower = np.array([0, 100, 100], dtype="uint8")
                        red_higher = np.array([30, 255, 255], dtype="uint8")
                        yellow_lower = np.array([31, 100, 100], dtype="uint8")
                        yellow_higher = np.array([60, 255, 255], dtype="uint8")
                        green_lower = np.array([61, 100, 100], dtype="uint8")
                        green_higher = np.array([90, 255, 255], dtype="uint8")
                        cyan_lower = np.array([91, 100, 100], dtype="uint8")
                        cyan_higher = np.array([120, 255, 255], dtype="uint8")
                        blue_lower = np.array([121, 100, 100], dtype="uint8")
                        blue_higher = np.array([150, 255, 255], dtype="uint8")
                        magenta_lower = np.array(
                            [151, 100, 100], dtype="uint8")
                        magenta_higher = np.array(
                            [179, 255, 255], dtype="uint8")
                        white_lower = np.array([0, 0, 100], dtype="uint8")
                        white_higher = np.array([0, 0, 255], dtype="uint8")
                        match request_json["payload"]["color"].lower():
                            case "red":
                                red = cv2.inRange(
                                    colorDetect, red_lower, red_higher)
                                if (cv2.countNonZero(red) > 100):
                                    gray_image = cv2.cvtColor(
                                        frame, cv2.COLOR_BGR2GRAY)
                                    # convert the grayscale image to binary image
                                    ret, thresh = cv2.threshold(
                                        gray_image, 127, 255, 0)
                                    # calculate moments of binary image
                                    M = cv2.moments(thresh)
                                    # calculate x,y coordinate of center
                                    cX = int(M["m10"] / M["m00"])
                                    cY = int(M["m01"] / M["m00"])
                                    print(cX, cY)
                                    break
                            case "yellow":
                                red = cv2.inRange(
                                    colorDetect, yellow_lower, yellow_higher)
                                if (cv2.countNonZero(red) > 100):
                                    gray_image = cv2.cvtColor(
                                        frame, cv2.COLOR_BGR2GRAY)
                                    # convert the grayscale image to binary image
                                    ret, thresh = cv2.threshold(
                                        gray_image, 127, 255, 0)
                                    # calculate moments of binary image
                                    M = cv2.moments(thresh)
                                    # calculate x,y coordinate of center
                                    cX = int(M["m10"] / M["m00"])
                                    cY = int(M["m01"] / M["m00"])
                                    print(cX, cY)
                                    break
                            case "green":
                                red = cv2.inRange(
                                    colorDetect, green_lower, green_higher)
                                if (cv2.countNonZero(red) > 100):
                                    gray_image = cv2.cvtColor(
                                        frame, cv2.COLOR_BGR2GRAY)
                                    # convert the grayscale image to binary image
                                    ret, thresh = cv2.threshold(
                                        gray_image, 127, 255, 0)
                                    # calculate moments of binary image
                                    M = cv2.moments(thresh)
                                    # calculate x,y coordinate of center
                                    cX = int(M["m10"] / M["m00"])
                                    cY = int(M["m01"] / M["m00"])
                                    print(cX, cY)
                                    break
                            case "blue":
                                red = cv2.inRange(
                                    colorDetect, blue_lower, blue_higher)
                                if (cv2.countNonZero(red) > 100):
                                    gray_image = cv2.cvtColor(
                                        frame, cv2.COLOR_BGR2GRAY)
                                    # convert the grayscale image to binary image
                                    ret, thresh = cv2.threshold(
                                        gray_image, 127, 255, 0)
                                    # calculate moments of binary image
                                    M = cv2.moments(thresh)
                                    # calculate x,y coordinate of center
                                    cX = int(M["m10"] / M["m00"])
                                    cY = int(M["m01"] / M["m00"])
                                    print(cX, cY)
                                    break
                            case "magenta":
                                red = cv2.inRange(
                                    colorDetect, magenta_lower, magenta_higher)
                                if (cv2.countNonZero(red) > 100):
                                    gray_image = cv2.cvtColor(
                                        frame, cv2.COLOR_BGR2GRAY)
                                    # convert the grayscale image to binary image
                                    ret, thresh = cv2.threshold(
                                        gray_image, 127, 255, 0)
                                    # calculate moments of binary image
                                    M = cv2.moments(thresh)
                                    # calculate x,y coordinate of center
                                    cX = int(M["m10"] / M["m00"])
                                    cY = int(M["m01"] / M["m00"])
                                    print(cX, cY)
                                    break
                            case "white":
                                red = cv2.inRange(
                                    colorDetect, white_lower, white_higher)
                                if (cv2.countNonZero(red) > 100):
                                    gray_image = cv2.cvtColor(
                                        frame, cv2.COLOR_BGR2GRAY)
                                    # convert the grayscale image to binary image
                                    ret, thresh = cv2.threshold(
                                        gray_image, 127, 255, 0)
                                    # calculate moments of binary image
                                    M = cv2.moments(thresh)
                                    # calculate x,y coordinate of center
                                    cX = int(M["m10"] / M["m00"])
                                    cY = int(M["m01"] / M["m00"])
                                    print(cX, cY)
                                    break

                    # LOAD AI DATA HERE
                    target_pixelX = cX
                    target_pixelY = cY

                    # Get current coordinates after finding target
                    geo = gps.geo_coords()
                    latitude = geo.lat
                    longitude = geo.lon

                    # LOAD GPS DATA HERE
                   # latitude = 33.837189
                   # longitude = -84.53877

                    # Create response with coordinates and pixels
                    response = {
                        "status": 200,
                        "message": "target_color",
                        "data": {
                            "latitude": latitude,
                            "longitude": longitude,
                            "target_X": target_pixelX,
                            "target_Y": target_pixelY,
                        }
                    }

                    # send response
                    string_json = json.dumps(response)
                    conn.sendall(string_json.encode('utf-8'))

                case "primary_status":
                    # Get coordinates
                    # geo = gps.geo_coords()
                    # latitude = geo.lat
                    # longitude = geo.lon

                    # PUT GPS DATA HERE
                    time.sleep(1)
                    latitude = round(random.uniform(-90, 91), 6)
                    longitude = round(random.uniform(-180, 181), 6)

                    # Create response
                    response = {
                        "status": 200,
                        "message": "primary_status",
                        "data": {
                            "latitude": latitude,
                            "longitude": longitude,
                        }
                    }
                    response_dump_string = json.dumps(response)

                    # Send the response
                    conn.sendall(response_dump_string.encode('utf-8'))

                case "target_found":
                    # send target coordinates to pada (port stuff)
                    # ...
                    # ...
                    time.sleep(1)
