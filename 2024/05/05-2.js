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

function checkOrder(inp) {
	let current = [];
	let good = true;
	for (let num = 0; num < inp.length; num++) {
		for (added of current) {
			if (order[inp[num]] && order[inp[num]].includes(added)) {
				good = false;
				break;
			}
		}
		if (!good) return num;
		current.push(inp[num]);
	}
	return -1;
}
let sum = 0;

inputs.forEach((inp) => {
	let rv = checkOrder(inp);

	if (rv != -1) {
		while (rv != -1) {
			[inp[rv], inp[rv - 1]] = [inp[rv - 1], inp[rv]];
			rv = checkOrder(inp);
		}
		// console.log("final, ", inp);
		sum += parseInt(inp[Math.floor(inp.length / 2)]);
	}
});

console.log(sum);
