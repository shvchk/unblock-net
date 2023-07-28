#! /usr/bin/env python3

import os
import glob
from pathlib import Path


apps = {
  'clash': 'generate_clash_list',
  'switchy-omega': 'generate_switchyomega_list'
}

lists = glob.glob('*.list')


def generate_clash_list(in_file, out_file):
  for line in in_file:
    if line[0] == '#' or line.strip() == '': continue
    out_file.write(f'+.{line}')


def generate_switchyomega_list(in_file, out_file):
  out_file.write('[SwitchyOmega Conditions]\n')

  for line in in_file:
    if line[0] == '#' or line.strip() == '': continue
    out_file.write(f'*.{line}')


os.chdir(Path(__file__).resolve().parent)

for app, fn in apps.items():
  print(f'Generating lists for {app}')
  for list_file in lists:
    filename = Path(list_file).stem
    out_path = Path(app) / filename
    in_file = open(list_file)
    out_file = open(out_path, 'w')

    print(f'- Generating {out_file}')
    locals()[fn](in_file, out_file)

    in_file.close()
    out_file.close()
