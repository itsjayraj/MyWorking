var fs = require("fs");

console.log("File reading");

var content = fs.readFileSync("./text.txt");

console.log(content.toString());
console.log("after reading file");
