#!/usr/bin/node
//Get the number of commind-line argiments passed
// Subtract 2 to exclude the "node" and script path arguments
// Print a message based on the number of arguments
const argsCount = process.argv.length - 2;
if (argsCount === 0) {
	console.log('No argument');
} else if (argsCount === 1) {
	console.log('Argument found');
} else {
	console.log('Argument found')
}
