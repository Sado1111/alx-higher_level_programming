#!/usr/bin/node
const arg1 = parseInt(process.argv[2]);
console.log(isNaN(arg1) ? 'Not a number' : arg1);
