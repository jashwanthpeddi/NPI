# -*- coding: utf-8 -*-
"""
Created on  Aug 22 05:23:05 2019

@author: Jashwanth Malipeddi
"""

################################### NPI scraper  #################################

from npyi import npi
import urllib.request, json
import time
import csv
import sys

f = open("sample_npi.csv", "r")
out_file = open("Output.csv", "w")
next(f)
for line in f.readlines():
    ref = line.split(',')
    npi_id = ref[3]
    response = npi.search(search_params={'number': npi_id})
    first_entry = response['results'][0]
    out_file.write(ref[0] + '\t' + ref[1] + '\t' + npi_id + '\t' +
                   ref[2] + '\t' + ref[4].rstrip() + '\t' + first_entry['addresses'][0]['city'] + '\t' +
                   first_entry['addresses'][0]['state'] + '\t' + first_entry['taxonomies'][0]['code'] + '\t' +
                   first_entry['taxonomies'][0]['desc'])
    out_file.write('\n')
out_file.close()