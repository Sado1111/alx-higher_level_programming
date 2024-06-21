#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) (c = 'x');
    for (let i = 0; i < this.height; i++) ('c'.repeat(this.width));
  }
}
module.exports = Square;
