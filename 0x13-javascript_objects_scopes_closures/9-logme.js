#!/usr/bin/node
// Prints the number of arguments already printed and the new argument value
let argLog = 0;
exports.logMe = function (item) {
  console.log(argLog + ': ' + item);
  argLog++;
};
