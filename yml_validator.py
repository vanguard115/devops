#!/usr/bin/env python3

import yaml
import sys

print("The YAML file being checked is %s" % (sys.argv[1]) )

file=sys.argv[1]




with open(file,'r') as stream:
    try:
        yaml.load(stream)
        print("Proper Syntax!!")
    except yaml.YAMLError as exc:
        print(exc)
