import argparse
import os

parser = argparse.ArgumentParser(
  prog="ls implemnet by Python"
)

parser.add_argument("-1", action="store_true", dest="one_per_line")
parser.add_argument("-a", action="store_true", dest="show_all")
parser.add_argument("paths", nargs="*")

args = parser.parse_args()

if not args.paths:
  args.paths = ["."]

for path in args.paths:
  if os.path.isdir(path):
    files = sorted(os.listdir(path))

    if not args.show_all:
      files = [file for file in files if not file.startswith(".")]

    if args.one_per_line:
      for file in files:
        print(file)
    else:
      for file in files:
        print(file, end="  ")
      print()
      
  else:
    print(path)