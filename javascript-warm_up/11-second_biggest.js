#!/usr/bin/node
const array = process.argv.slice(2);
const length = process.argv.length;
if (length <= 3) {
  console.log(0);
} else {
  array.sort((a, b) => b - a);
  console.log(array[1]);
}
