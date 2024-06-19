#!/usr/bin/node
const argsLen = process.argv.length;
console.log(argsLen === 2 ? 'No argument' : argsLen === 3 ? 'Argument found' : 'Arguments found');
