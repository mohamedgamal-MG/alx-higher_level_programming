#!/usr/bin/node
const argc = parseInt(process.argv[2]);
console.log(argc ?  `My number: ${argc}` : 'Not a number');
