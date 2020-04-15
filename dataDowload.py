#!/usr/bin/python
#!python

import urllib.request
from datetime import date


def dowload_dataset(urldescarga, pathdestino):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print('[', d1, ']', 'downloading dataset...')

    urllib.request.urlretrieve(urldescarga, pathdestino)
