#!/usr/bin/env python3

import sys
import argparse

print("Hello, this is a test to run it via shebang")
print(sys.version)

parser = argparse.ArgumentParser()
parser.parse_args()