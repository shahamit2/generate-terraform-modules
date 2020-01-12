#!/usr/bin/env python3

import hcl
import sys
from json import dumps


class GenerateTFModules:

    def __init__(self, var_file):
        self.tfvar_file = open(tfvar_file, 'r',  encoding='utf-8')
        self.tfvar_dict = hcl.load(self.tfvar_file)

    def generate_sg_rules(self):
        module_source = "./sg-rules"
        if 'sg_list' not in self.tfvar_dict:
            return
        else:
            print("\n-> Generating sg-rules.tf for SG Rules.. ")
        target_file = open("sg-rules.tf", "w+")
        for sg in self.tfvar_dict['sg_list']:
          counter = 1
          for tr in sg['traffic_rules']:
              target_file.write("module sg_" + sg['name'] + "_rule" + str(counter) + " {\n")
              target_file.write('  source = "' + module_source + '"\n')
              target_file.write('  create_sg  = var.create_sg\n')
              target_file.write('  sg_name = "' + sg['name'] + '"\n')
              target_file.write('  type = "' + tr['type'] + '"\n')
              target_file.write("  rule_list = " + dumps(tr['rule_list']) + "\n")
              target_file.write('  ref_sg_name = "' + tr['ref_sg_name'] + '"\n')
              target_file.write('  sg_name_id = module.sg.sg_name_id' + '\n')
              target_file.write('}\n')
              target_file.write('\n')
              counter = counter + 1
        target_file.close()
        print("Done.")
        print("================")


if __name__ == "__main__":
   if len(sys.argv) < 2:
      print("Please supply '.tfvars' file as parameter!!!")
      exit()
   tfvar_file  = sys.argv[1]
   g = GenerateTFModules(tfvar_file)
   g.generate_sg_rules()
