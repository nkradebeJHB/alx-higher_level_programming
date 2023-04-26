#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.
const request = require('request');
const url = process.argv[2];
const fs = require('fs');
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
