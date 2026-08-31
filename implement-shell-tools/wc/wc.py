import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-l", action="store_true")
parser.add_argument("-w", action="store_true")
parser.add_argument("-c", action="store_true")
parser.add_argument("files", nargs="+")

args = parser.parse_args()


def add_count(output, value):
  output.append(str(value))


total_lines = 0
total_words = 0
total_bytes = 0

for filename in args.files:

  with open(filename, "rb") as file:
    content = file.read()

  lines = content.count(b"\n")
  words = len(content.split())
  bytes_count = len(content)

  total_lines += lines
  total_words += words
  total_bytes += bytes_count

  if not args.l and not args.w and not args.c:
    print(f"{lines:8} {words:8} {bytes_count:8} {filename}")

  else:
    output = []

    if args.l:
      add_count(output, lines)

    if args.w:
      add_count(output, words)

    if args.c:
      add_count(output, bytes_count)

    print(f"{' '.join(output):>8} {filename}")

