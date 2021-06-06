#!/usr/bin/python3

import os, psutil
import xml.etree.ElementTree as ET

def report_mem_usage(description):
	process = psutil.Process(os.getpid())
	print(f"{description}, memory usage is {round(process.memory_info().rss/1024/1024,2)} MB")  # in bytes 

report_mem_usage("Startup")

tree = ET.parse('input.xml')

root = tree.getroot()

dataitems = []

for item in root.findall('./data'):
	dataitems.append(item.text)

dataitem_count = 0
for dataitem in dataitems:
	dataitem_count = dataitem_count + 1

print(f"Items loaded: {dataitem_count}")

report_mem_usage("Finished parsing and loading XML data")