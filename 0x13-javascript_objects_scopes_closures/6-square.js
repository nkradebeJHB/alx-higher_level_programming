#!/usr/bin/node
// a class Square that defines a square and
// inherits from Square.

const square = require('./5-square');

// inherint from Square
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  // method that prints the rectangle using the character c
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let charec;
    for (let i = 0; i < this.height; i++) {
      charec = '';
      for (let j = 0; j < this.width; j++) {
        charec += c;
      }
      console.log(charec);
    }
  }
}

module.exports = Square;
