#Author: Vito Andika Mulia
#Purpose: ACO331 (Network Forensic Analysis) - Project 4

import random
import sys

def readFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def print_random_records(records, count=100):
    count = min(count, len(records))
    
    random_records = random.sample(records, count)
    
    for record in random_records:
        print(record)

def main():
    if len(sys.argv) < 2:
        print("Usage: python 100-random-records.py <netflow-file>")
        sys.exit(1)

    filename = sys.argv[1]
    
    if not filename.endswith('.txt'):
        print("Error: please specify a .txt file")
        sys.exit(1)

    netflow_records = readFile(filename)

    # Print 100 random NetFlow records
    print_random_records(netflow_records)

if __name__ == "__main__":
    main()
