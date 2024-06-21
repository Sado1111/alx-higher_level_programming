#!/usr/bin/node

const SquareBase = require('./5-square.js');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) (c = 'x');
    for (let i = 0; i < this.height; i++) ('c'.repeat(this.width));
  }
}
module.exports = Square;
