#!/usr/local/bin/python

import argparse

parser = argparse.ArgumentParser(description='Treinuren voor een bepaald traject')
parser.add_argument('FROM', help='beginstation van de reis')
parser.add_argument('TO', help='eindstation van de reis')

args = parser.parse_args()

print(args.TO)
