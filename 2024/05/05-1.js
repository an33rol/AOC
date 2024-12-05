const path = require("path");
const file = path.join(__dirname, "/05.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n");
let order = {};
let inputs = [];
let things = false;

data.forEach((line, index) => {
	if (line.length == 0) {
		things = true;
		return;
	}
	if (!things) {
		let key = line.split("|")[0];
		let value = line.split("|")[1];
		if (order[key]) order[key].push(value);
		else order[key] = [value];
	} else {
		inputs.push(line.split(","));
	}
});
let sum = 0;

inputs.forEach((inp) => {
	let current = [];
	let good = true;
	for (num of inp) {
		for (added of current) {
			if (order[num] && order[num].includes(added)) {
				good = false;
				break;
			}
		}
		if (!good) break;
		current.push(num);
	}
	if (good) {
		sum += parseInt(inp[Math.floor(inp.length / 2)]);
	}
});

console.log(sum);
