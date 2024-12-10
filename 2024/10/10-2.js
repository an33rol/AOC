const path = require("path");
const file = path.join(__dirname, "/10.txt");
const fs = require("node:fs");
const { start } = require("repl");
const { read } = require("fs");

const map = fs
	.readFileSync(file, "utf8")
	.split("\n")
	.map((line) => line.split("").map((char) => parseInt(char)));
let sum = 0;
let wid = map.length;

let dirs = [
	[0, 1],
	[0, -1],
	[1, 0],
	[-1, 0],
];

function checkPath(it, jt, time) {
	while (true) {
		// console.log(it, jt, time);

		if (map[it][jt] == 9) {
			return true;
		}

		if (time >= 10) {
			return false;
		}

		let good = [];
		// find  all possible directions
		for (let k = 0; k < dirs.length; k++) {
			try {
				if (map[it + dirs[k][0]][jt + dirs[k][1]] == map[it][jt] + 1) {
					good.push(k);
				}
			} catch (e) {}
		}

		// cant proceed
		if (good.length == 0) {
			return false;
		}

		// recursion;
		for (let k = 0; k < good.length - 1; k++) {
			if (checkPath(it + dirs[good[k]][0], jt + dirs[good[k]][1], time + 1))
				sum++;
		}

		time++;
		it += dirs[good[good.length - 1]][0];
		jt += dirs[good[good.length - 1]][1];
	}
}

for (let i = 0; i < map.length; i++) {
	for (let j = 0; j < map.length; j++) {
		if (map[i][j] == 0) {
			if (checkPath(i, j, 0)) sum++;
		}
	}
}

console.log("sum", sum);
