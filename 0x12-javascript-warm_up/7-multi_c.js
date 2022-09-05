#!/usr/bin/node
// prints x times “C is fun”.

const x = process.argv[2];

if (!x) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
