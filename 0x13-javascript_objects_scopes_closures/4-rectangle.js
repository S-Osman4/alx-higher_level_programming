#!/usr/bin/nodejs
// Print, rotate and multiplies the rectangle.
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let s = this.height; s; s--) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temporary = this.width;
    this.width = this.height;
    this.height = temporary;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
