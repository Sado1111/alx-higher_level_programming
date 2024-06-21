#!/usr/bin/node

const list = require('./100-data.js').lists;
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
