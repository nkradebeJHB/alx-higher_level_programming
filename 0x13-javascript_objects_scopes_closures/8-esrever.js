#!/usr/bin/node
// A function that returns the reversed version of a list:

exports.esrever = function (list) {
  const revList = [];
  while (list.length) {
    revList.push(list.pop());
  }
  return revList;
};
