import argparse


parser = argparse.ArgumentParser(
  prog="cat implemnet by Python"
)

parser.add_argument("-n", action="store_true")
parser.add_argument("-b", action="store_true")
parser.add_argument("files", nargs="+")

args = parser.parse_args()

line_number = 1

for filename in args.files:
   
  with open(filename) as file:
    for line in file:
      line = line.rstrip("\n")

      if args.b and line == "":
        print()
        continue

      if args.n or args.b:
        print(f"{line_number} {line}")
        line_number += 1
      else:
        print(line)