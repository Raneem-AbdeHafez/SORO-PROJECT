# -*- coding: utf-8 -*-
"""Shared NAO defaults used by the robot scripts."""
import os
IP = "your robot's IP address"
DEFAULT_NAO_IP = os.environ.get("NAO_IP", IP)
DEFAULT_NAO_PORT = int(os.environ.get("NAO_PORT", "9559"))
