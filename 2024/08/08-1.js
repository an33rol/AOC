const path = require("path");
const file = path.join(__dirname, "/07.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n");
let sum = 0;
data.forEach((line) => {});

console.log(sum);
