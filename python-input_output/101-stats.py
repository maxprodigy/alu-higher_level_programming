#!/usr/bin/python3
'''
Reading data from stdout
'''
import sys
import re


def print_data(code_count, total_size):
    '''
    Prints data summary
    '''
    print("File size: {}".format(total_size))
    for key, value in sorted(code_count.items()):
        if value > 0:
            print("{key}: {value}".format(key=key, value=value))


i = 0
pattern = (r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/(\d+) '
           r'HTTP/\d\.\d" (\d+) (\d+)')
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
try:
    for line in sys.stdin:
        i += 1
        match = re.match(pattern, line)
        if match:
            ip_address = match.group(1)
            date = match.group(2)
            project_id = match.group(3)
            status_code = match.group(4)
            file_size = match.group(5)

        status_code_counts[int(status_code)] += 1
        total_file_size += int(file_size)
        if i == 10:
            i = 0
            print_data(status_code_counts, total_file_size)
except KeyboardInterrupt:
    print_data(status_code_counts, total_file_size)
