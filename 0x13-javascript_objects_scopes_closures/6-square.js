#!/usr/bin/nodejs
// defines a square and inherits from Square Class.
const Square2 = require('./5-square.js');

module.exports = class Square extends Square2 {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let j = this.height; j; j--) {
      console.log(c.repeat(this.width));
    }
  }
};
