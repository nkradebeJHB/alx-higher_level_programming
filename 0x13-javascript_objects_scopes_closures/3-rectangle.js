#!/usr/bin/node
// A Rectangle class that prints a rectangle

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let charec;
    for (let i = 0; i < this.height; i++) {
      charec = '';
      for (let j = 0; j < this.width; j++) {
        charec += 'X';
      }
      console.log(charec);
    }
  }
}
module.exports = Rectangle;
