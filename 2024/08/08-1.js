const path = require("path");
const file = path.join(__dirname, "/08.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n");
let dict = {};
let sum = 0;

// mark all locations
for (let i = 0; i < data.length; i++) {
	for (let j = 0; j < data.length; j++) {
		if (data[i][j].match(/\w/)) {
			if (dict[data[i][j]]) {
				dict[data[i][j]].push([i, j]);
			} else {
				dict[data[i][j]] = [[i, j]];
			}
		}
	}
}

//iterate
let options = [];
for (key of Object.keys(dict)) {
	for (let k = 0; k < dict[key].length; k++) {
		for (let l = k + 1; l < dict[key].length; l++) {
			let pos1 = dict[key][k];
			let pos2 = dict[key][l];
			if (pos1 != pos2) {
				// x = i, y = j
				let xdis = Math.abs(pos1[0] - pos2[0]);
				let ydis = Math.abs(pos1[1] - pos2[1]);
				let node1 = [
					Math.min(pos1[0], pos2[0]) - xdis,
					pos1[1] < pos2[1] ? pos1[1] - ydis : pos1[1] + ydis,
				];
				let node2 = [
					Math.max(pos1[0], pos2[0]) + xdis,
					pos2[1] < pos1[1] ? pos2[1] - ydis : pos2[1] + ydis,
				];
				options.push(node1);
				options.push(node2);
			}
		}
	}
}

console.log(
	new Set(
		options
			.filter(
				(pos) =>
					pos[0] >= 0 &&
					pos[0] < data.length &&
					pos[1] >= 0 &&
					pos[1] < data.length
			)
			.map((pos) => pos[0] * data.length + pos[1])
	).size
);
