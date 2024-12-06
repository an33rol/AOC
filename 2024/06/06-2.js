const path = require("path");
const file = path.join(__dirname, "/06.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n");
const wid = data[0].length;
let dirs = [
	[-1, 0],
	[0, 1],
	[1, 0],
	[0, -1],
];
let diri = 0;
let starti = null;
let startj = null;
let passed = [];

// find starting position
for (let k = 0; k < data.length; k++) {
	const found = data[k].match(/\^/);
	if (found) {
		startj = found.index;
		starti = k;

		break;
	}
}

// find path
let i = starti;
let j = startj;
for (let k = 0; ; k++) {
	try {
		step = dirs[diri];

		if (data[i + step[0]][j + step[1]] != "#") {
			i += step[0];
			j += step[1];
			passed.push([i, j]);
		} else {
			diri = (diri + 1) % 4;
		}
	} catch (e) {
		break;
	}
}
passed.pop([starti, startj]);

function isItLoop(it, jt, obsi, obsj) {
	// walk
	diri = 0;
	let visited = new Set([jt + it * wid + diri * wid * wid]);

	for (let k = 0; ; k++) {
		let step = dirs[diri];
		if (
			it + step[0] < 0 ||
			jt + step[1] < 0 ||
			it + step[0] >= wid ||
			jt + step[1] >= wid
		) {
			return false;
		}
		if (
			(obsi != it + step[0] || obsj != jt + step[1]) &&
			data[it + step[0]][jt + step[1]] != "#"
		) {
			it += step[0];
			jt += step[1];
			if (visited.has(jt + it * wid + diri * wid * wid)) {
				return true;
			}
			visited.add(jt + it * wid + diri * wid * wid);
		} else {
			diri = (diri + 1) % 4;
		}
	}
}

let count = 0;
let checked = new Set();
for (pos of passed) {
	if (
		!checked.has(pos[0] * wid + pos[1]) &&
		isItLoop(starti, startj, pos[0], pos[1])
	) {
		count++;
	}
	checked.add(pos[0] * wid + pos[1]);
}

console.log(count);
