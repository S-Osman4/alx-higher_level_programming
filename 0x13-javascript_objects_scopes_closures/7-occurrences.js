#!/usr/bin/nodejs
// function that returns the number of occurrences in a list.
exports.nbOccurences = function (list, searchElement) {
  let container = 0;
  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      container += 1;
    }
  }
  return (container);
};
