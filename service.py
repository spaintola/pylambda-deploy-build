# -*- coding: utf-8 -*-

import requests
import pg8000

def handler(event, context):
    # Your code goes here!
    e = event.get("e")
    pi = event.get("pi")
    return e + pi
