#!/usr/bin/node
// A script that display the status code of a GET request.
const request = require('request');
request
  .get(process.argv[2])
  .on('res', function (res) {
    console.log('code: ' + res.statusCode);
  });
