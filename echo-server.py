#!/usr/bin/env python3

import socket
import time
import json
import random
import subprocess
import serial

from ublox_gps import UbloxGps

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65438  # Port to listen on (non-privileged ports are > 1023)
BASE_STATION_ADDRESS = "10.0.0.2"  # U-center NTRIP server address

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

                    # LOAD AI DATA HERE
                    target_pixelX = 2000
                    target_pixelY = 1125

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
                    # PUT GPS DATA HERE
                    geo = gps.geo_coords()
                    latitude = geo.lat
                    longitude = geo.lon

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

                # case "target_found":
                    # send target coordinates to pada (port stuff)
                    # ...
                    # ...
                    # time.sleep(1)
