const path = require("path");
const file = path.join(__dirname, "/06.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n");
const wid = data[0].length;
let visited = new Set();
let dirs = [
	[-1, 0],
	[0, 1],
	[1, 0],
	[0, -1],
];
let diri = 0;
let j = null;
let i = null;

// find starting position
for (let k = 0; k < data.length; k++) {
	const found = data[k].match(/\^/);
	if (found) {
		j = found.index;
		i = k;
		visited.add(j + i * wid);

		break;
	}
}

// walk
for (let k = 0; ; k++) {
	try {
		step = dirs[diri];

		if (data[i + step[0]][j + step[1]] != "#") {
			i += step[0];
			j += step[1];
			visited.add(j + i * wid);
		} else {
			diri = (diri + 1) % 4;
		}
	} catch (e) {
		break;
	}
}

console.log(visited.size);
