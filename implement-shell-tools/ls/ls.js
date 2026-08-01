import { readdir, stat } from "node:fs/promises";
import process from "node:process";

const argv = process.argv.slice(2);

let onePerLine = false;
let showAll = false;
const paths = [];

for (const arg of argv) {
  if (arg === "-1") {
    onePerLine = true;
  } else if (arg === "-a") {
    showAll = true;
  } else {
    paths.push(arg);
  }
}

if (paths.length === 0) {
  paths.push(".");
}

for (const path of paths) {
  try {
    const info = await stat(path);

    if (info.isDirectory()) {
      let files = await readdir(path);

      if (!showAll) {
        files = files.filter((file) => !file.startsWith("."));
      }

      if (onePerLine) {
        for (const file of files) {
          console.log(file);
        }
      } else {
        for (const file of files) {
          process.stdout.write(`${file}  `);
        }
        process.stdout.write("\n");
      }
    } else {
      console.log(path);
    }
  } catch (err) {
    console.error(err.message);
  }
}