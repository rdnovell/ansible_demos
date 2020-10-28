#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys

if __name__ == '__main__':
  fields = {
    "yourName": {"required": True, "type": "str"}
  }
  module = AnsibleModule(argument_spec=fields)
  yourName = os.path.expanduser(module.params['yourName'])
  output = "Hola soy el custom module de python " + yourName
  module.exit_json(msg=output)