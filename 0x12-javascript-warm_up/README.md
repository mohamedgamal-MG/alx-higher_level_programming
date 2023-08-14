```markdown
# JavaScript Warm-Up

This repository contains a set of JavaScript scripts that cover various warm-up exercises to help you get familiar with JavaScript programming concepts.

## Table of Contents

1. [First constant, first print](#first-constant-first-print)
2. [3 languages](#3-languages)
3. [Arguments](#arguments)
4. [Value of my argument](#value-of-my-argument)
5. [Create a sentence](#create-a-sentence)
6. [An Integer](#an-integer)
7. [Loop to languages](#loop-to-languages)
8. [I love C](#i-love-c)
9. [Square](#square)
10. [Add](#add)
11. [Factorial](#factorial)
12. [Second biggest!](#second-biggest)
13. [Object](#object)
14. [Add file](#add-file)
15. [Const or not const](#const-or-not-const)
16. [Call me Moby](#call-me-moby)
17. [Add me maybe](#add-me-maybe)
18. [Increment object](#increment-object)

## Task Descriptions

### First constant, first print

Write a script that prints "JavaScript is amazing":

- Create a constant variable called `myVar` with the value "JavaScript is amazing"
- Use `console.log(...)` to print the output
- You are not allowed to use `var`

```bash
$ ./0-javascript_is_amazing.js
JavaScript is amazing
```

### 3 languages

Write a script that prints three lines:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- Use `console.log(...)` to print all output
- You are not allowed to use `var`

```bash
$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
```

### Arguments

Write a script that prints a message depending on the number of arguments passed:

- If no arguments are passed to the script, print "No argument"
- If only one argument is passed to the script, print "Argument found"
- Otherwise, print "Arguments found"
- Use `console.log(...)` to print the output
- Reference: `process.argv`

```bash
$ ./2-arguments.js
No argument
$ ./2-arguments.js Best
Argument found
$ ./2-arguments.js Best School
Arguments found
```

### Value of my argument

Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print "No argument"
- Use `console.log(...)` to print the output
- You are not allowed to use `var`
- You are not allowed to use `length`

```bash
$ ./3-value_argument.js
No argument
$ ./3-value_argument.js School
School
```

### Create a sentence

Write a script that prints two arguments passed to it, in the following format: " is "

- Use `console.log(...)` to print the output

```bash
$ ./4-concat.js c cool
c is cool
$ ./4-concat.js c 
c is undefined
$ ./4-concat.js
undefined is undefined
```

### An Integer

Write a script that prints "My number: <first argument converted to an integer>" if the first argument can be converted to an integer:

- If the argument can't be converted to an integer, print "Not a number"
- Use `console.log(...)` to print the output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`

```bash
$ ./5-to_integer.js 
Not a number
$ ./5-to_integer.js 89
My number: 89
$ ./5-to_integer.js "89"
My number: 89
$ ./5-to_integer.js 89.89
My number: 89
$ ./5-to_integer.js School
Not a number
```

### Loop to languages

Write a script that prints three lines using an array of strings and a loop:

- The first line: "C is fun"
- The second line: "Python is cool"
- The third line: "JavaScript is amazing"
- Use `console.log(...)` to print the output
- You are not allowed to use `var`
- You are not allowed to use any if/else statement
- You can use only one `console.log`
- You must use a loop (while, for, etc.)

```bash
$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
```

### I love C

Write a script that prints "C is fun" x times:

- Where x is the first argument of the script
- If the first argument can't be converted to an integer, print "Missing number of occurrences"
- Use `console.log(...)` to print the output
- You are not allowed to use `var`
- You must use a loop (while, for, etc.)

```bash
$ ./7-multi_c.js 2
C is fun
C is fun
$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
$ ./7-multi_c.js 
Missing number of occurrences
$ ./7-multi_c.js -3
```

### Square

Write a script that prints a square:

- The first argument is the size of the square
- If the first argument can't be converted to an integer, print "Missing size"
- Use the character 'X' to print the square
- Use `console.log(...)` to print the output
- You are not allowed to use `var`
- You must use a loop (while, for, etc.)

```bash
$ ./8-square.js
Missing size
$ ./8-square.js School
Missing size
$ ./8-square.js 2
XX
XX
$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
$ ./8-square.js -3
```

### Add

Write a script that prints the addition of two integers:

- The first argument is the first integer
- The second argument is the second integer
- You must define a function with this prototype: `function add(a, b)`
- Use `console.log(...)` to print the output
- You are not allowed to use `var`

```bash
$ ./9-add.js 
NaN
$ ./9-add.js 1
NaN
$ ./9-add.js 1 7
8
$ ./9-add.js 13 89
102
```

### Factorial

Write a script that computes and prints a factorial:

- The first argument is an integer used for computing the factorial
- The factorial of NaN is 1
- You must do it recursively
- You must use a function
- Use `console.log(...)` to print the output
- You are not allowed to use `var`

```bash
$ ./10-factorial.js 
1
$ ./10-factorial.js 3
6
$ ./10-factorial.js 89


1.6507955160908452e+136
```

### Second biggest!

Write a script that searches for the second biggest integer in the list of arguments:

- You can assume all arguments can be converted to integers
- If no argument is passed, print 0
- If the number of arguments is 1, print 0
- Use `console.log(...)` to print the output
- You are not allowed to use `var`

```bash
$ ./11-second_biggest.js 
0
$ ./11-second_biggest.js 1
0
$ ./11-second_biggest.js 4 2 5 3 0 -3
4
```

### Object

Update this script to replace the value 12 with 89:

```javascript
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);
```

```bash
$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
```

### Add file

Write a function that returns the addition of two integers:

- The function must be visible from outside
- The name of the function must be `add`

```javascript
// 13-add.js
exports.add = function (a, b) {
  return a + b;
};
```

```javascript
// 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
```

```bash
$ ./13-main.js
8
```

### Const or not const

Write a file that modifies the value of `myVar` to 333:

```javascript
// 100-let_me_const.js
#!/usr/bin/node
myVar = 333;
```

```javascript
// 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
```

```bash
$ ./100-main.js
333
```

### Call me Moby

Write a function that executes a function `x` times:

- The function must be visible from outside
- Prototype: `function (x, theFunction)`

```javascript
// 101-call_me_moby.js
#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
```

```javascript
// 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
```

```bash
$ ./101-main.js
C is fun
C is fun
C is fun
```

### Add me maybe

Write a function that increments and calls a function:

- The function must be visible from outside
- Prototype: `function (number, theFunction)`

```javascript
// 102-add_me_maybe.js
#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
```

```javascript
// 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
```

```bash
$ ./102-main.js
New value: 5
```

### Increment object

Update this script by adding a new function `incr` that increments the integer value:

```javascript
// 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
```

```bash
$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
```

## Contributing

If you find any issues or improvements with these scripts, feel free to contribute by opening an issue or a pull request in the [GitHub repository](https://github.com/your-username/alx-higher_level_programming).
```

Remember to replace `your-username` with your actual GitHub username. You can add this README.md file to your repository's root directory (0x12-javascript-warm_up) and commit it along with your code.
