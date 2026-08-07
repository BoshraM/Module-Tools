import { readFile } from "node:fs/promises";
import process from "node:process";

const argvs= process.argv.slice(2);
let countLines = false;
let countWords = false;
let countBytes = false;
let totalWords = 0;
let totalLines = 0;
let totalBytes = 0;
const files = []

for (const arg of argvs) {
  if (arg === "-l") {
    countLines = true;
  } else if (arg === "-w") {
    countWords = true;
  } else if (arg === "-c") {
    countBytes = true;
  } else {
    files.push(arg);
  }
}

for (const file of files) {
  try {
    const content = await readFile(file, "utf-8");
    const arrayOfLines = content.split("\n");
    const arrayOfWords = content.trim().split(/\s+/)
    const bytes = Buffer.byteLength(content, "utf-8");
    const lines = arrayOfLines.length -1;
    const words = arrayOfWords.length;
    totalLines += lines;
    totalBytes += bytes;
    totalWords +=words
    if (countLines && countWords) {
      process.stdout.write(`       ${lines}      ${words} ${file}\n`);

    } else if (countLines) {
      process.stdout.write(`       ${lines} ${file}\n`);
      
    } else if (countWords){
      process.stdout.write(`  ${words} ${file}\n`);

    } else if (countBytes) {
      process.stdout.write(`   ${bytes} ${file}\n`);

    } else {
      process.stdout.write(`       ${lines}      ${words}      ${bytes} ${file}\n`);
    }
      
  } catch(err) {
    console.error(err.message);
  }
}

if (files.length > 1 ) {
  if (countLines && countWords) {
    process.stdout.write(`       ${totalLines}      ${totalWords} total\n`);

  } else if (countLines) {
    process.stdout.write(`       ${totalLines} total\n`);
    
  } else if (countWords){
    process.stdout.write(`  ${totalWords} total\n`);

  } else if (countBytes) {
    process.stdout.write(`   ${totalBytes} total\n`);

  } else {
    process.stdout.write(`       ${totalLines}      ${totalWords}      ${totalBytes} total\n`);
  }
}





