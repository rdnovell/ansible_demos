#!/bin/env python
from ansible.module_utils.basic import *
import os, json
import re, sys

if __name__ == '__main__':
   arguments = dict(
     name=dict(required=True)
     )

  module = AnsibleModule(argument_spec=arguments)
  yourName = module.params['name']
  output = "Hola soy el custom module de python " + yourName
  module.exit_json(msg=output)