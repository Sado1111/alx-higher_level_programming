#!/usr/bin/node

const SquareBase = require('./4-rectangle.js').Rectangle;

class Square extends SquareBase {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
