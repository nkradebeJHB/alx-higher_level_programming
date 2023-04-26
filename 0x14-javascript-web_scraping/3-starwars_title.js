#!/usr/bin/node
// A script that prints the title of a Star Wars movie.
const request = require('request');
request(`http://swapi.co/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
