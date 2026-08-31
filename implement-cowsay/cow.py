import argparse
import cowsay

parser = argparse.ArgumentParser(
  prog="cowsay",
  description="Make an animal say something"
)

parser.add_argument(
  "message",
  nargs="+",
  help="What do you want the animal to say?"
)

parser.add_argument(
  "--animal",
  choices=cowsay.char_names,
  default="cow",
  help="Choose an animal"
)

args = parser.parse_args()

message = " ".join(args.message)

print(cowsay.get_output_string(args.animal, message))