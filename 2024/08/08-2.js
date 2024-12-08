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

let options = [];

for (key of Object.keys(dict)) {
	// add all existing antenas
	if (dict[key].length != 1) {
		options.push(...dict[key]);
	}

	for (let k = 0; k < dict[key].length; k++) {
		for (let l = k + 1; l < dict[key].length; l++) {
			let pos1 = dict[key][k];
			let pos2 = dict[key][l];
			let pushed = true;
			let factor = 1;
			if (pos1 != pos2) {
				while (pushed) {
					// x = i, y = j
					let xdis = Math.abs(pos1[0] - pos2[0]);
					let ydis = Math.abs(pos1[1] - pos2[1]);
					let node1 = [
						Math.min(pos1[0], pos2[0]) - factor * xdis,
						pos1[1] < pos2[1]
							? pos1[1] - factor * ydis
							: pos1[1] + factor * ydis,
					];
					let node2 = [
						Math.max(pos1[0], pos2[0]) + factor * xdis,
						pos2[1] < pos1[1]
							? pos2[1] - factor * ydis
							: pos2[1] + factor * ydis,
					];
					// check if fit
					let nodes = [node1, node2].filter(
						(pos) =>
							pos[0] >= 0 &&
							pos[0] < data.length &&
							pos[1] >= 0 &&
							pos[1] < data.length
					);
					if (nodes.length != 0) {
						options.push(...nodes);
					} else {
						pushed = false;
					}
					factor++;
				}
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
