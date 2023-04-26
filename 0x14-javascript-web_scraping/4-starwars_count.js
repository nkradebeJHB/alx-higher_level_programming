#!/usr/bin/node
// A script that prints the number of movies where the
// character “Wedge Antilles” is present.
const request = require('request');
const find = '/18/';
request(process.argv[2], function (err, response, body) {
  if (err) throw new Error(err);
  let num = 0;
  for (const i of JSON.parse(body).results) {
    for (const character of i.characters) {
      num += (character.includes(find) ? 1 : 0);
    }
  }
  console.log(num);
});
