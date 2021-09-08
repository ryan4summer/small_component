#!/usr/bin/env python3

import requests


response = requests.get("http://api.open-notify.org/astros.json")

print(response.status_code)