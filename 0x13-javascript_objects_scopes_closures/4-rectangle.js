#!/usr/bin/node
// A Rectangle class that prints, rotates 
// and doubles a rectangle

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

 // swap the width and tha height to rotate
 rotate () {
    const swap = this.width;
    this.width = this.height;
    this.height = swap;
  }

 // Double the rectangle
 double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
