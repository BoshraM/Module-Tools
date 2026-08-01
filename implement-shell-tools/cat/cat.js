import { readFile } from "node:fs/promises";
import process from "node:process";

const argv = process.argv.slice(2);

let showLineNumbers = false;
let numberNonBlankLines = false;
const files = [];

for (const arg of argv) {
  if (arg === "-n") {
    showLineNumbers = true;
  } else if (arg === "-b") {
    numberNonBlankLines = true;
  } else {
    files.push(arg);
  }
}

let lineNumber = 1;

for (const file of files) {
  try {
    const content = await readFile(file, "utf-8");

    const lines = content.split("\n");

    if (numberNonBlankLines) {
      for (const line of lines) {
        if (line !== "") {
          console.log(`${lineNumber} ${line}`);
          lineNumber++;
        } else {
          console.log("");
        }
      }
    } else if (showLineNumbers) {
      for (const line of lines) {
        console.log(`${lineNumber} ${line}`);
        lineNumber++;
      }
    } else {
      process.stdout.write(content);
    }
  } catch (err) {
    console.error(err.message);
  }
}