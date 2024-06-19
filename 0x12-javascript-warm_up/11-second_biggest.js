#!/usr/bin/node
const argArr = process.argv.slice(2).sort((a, b) => b - a).map(Number);
if (argArr.length <= 1) console.log('0');
else console.log(argArr[1]);
