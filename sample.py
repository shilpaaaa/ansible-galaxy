#!/usr/bin/env python
import os
import sys
import json
def example_inventory():
 return{'group':{'hosts': ['35.231.254.233']}};
inventory=example_inventory()
print json.dumps(inventory);
