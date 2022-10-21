#!/usr/bin/node
const request = require('request');
if (process.argv.length > 2) {
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const count = JSON.parse(body).results.filter(item => item.characters.find(id => id.match(/18/)));
      console.log(count.length);
    }
  });
}
