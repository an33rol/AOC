const path = require("path");
const file = path.join(__dirname, "/11.txt");
const fs = require("node:fs");
const { start } = require("repl");
const { read } = require("fs");
const { listenerCount } = require("process");

let initvalues = fs
	.readFileSync(file, "utf8")
	.split("\n")[0]
	.split(" ")
	.map((c) => parseInt(c));

function process(elem) {
	if (elem == 0) {
		return [1];
	}
	elem = elem.toString();
	leng = elem.length;
	if (leng % 2 == 0) {
		return [
			parseInt(elem.slice(0, leng / 2)),
			parseInt(elem.slice(-leng / 2)),
		];
	}
	return [elem * 2024];
}

// blink
let blinks = 75;

for (elem of initvalues) {
	list = [elem];
	for (let b = 0; b < blinks; b++) {
		n = [];
		for (let elm of list) {
			n.push(...process(elm));
		}
		list = n;
	}
	sum += list.length;
}

console.log("len", sum);
