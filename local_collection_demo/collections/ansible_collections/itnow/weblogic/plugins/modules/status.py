#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys

if __name__ == '__main__':
  module = AnsibleModule(argument_spec={})
  output = "Hola soy un falso status" 
  module.exit_json(msg=output)