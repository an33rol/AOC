const path = require("path");
const file = path.join(__dirname, "/12.txt");
const fs = require("node:fs");

class Area {
	constructor(tileid, per) {
		this.tiles = new Set([tileid]);
		this.perimiter = per;
		this.price = 0;
	}
}

let map = fs
	.readFileSync(file, "utf8")
	.split("\n")
	.map((line) => line.split(""));

let areas = [];
let wid = map.length;
let dirs = [
	[0, 1],
	[0, -1],
	[1, 0],
	[-1, 0],
];

function calcPer(i, j) {
	let char = map[i][j];
	let num = 4;
	for (let dir of dirs) {
		if (
			i + dir[0] < wid &&
			j + dir[1] < wid &&
			i + dir[0] >= 0 &&
			j + dir[1] >= 0
		)
			num -= map[i + dir[0]][j + dir[1]] == char;
	}
	return num;
}

function add(i, j, nbid) {
	if (i < 0 || j < 0 || j >= wid || i >= wid) return false;

	let id = i * wid + j;
	let added = false;

	for (let area of areas) {
		// already added
		if (area.tiles.has(id)) return false;

		// add
		if (area.tiles.has(nbid)) {
			area.tiles.add(id);
			area.perimiter += calcPer(i, j);
			added = true;
		}
	}
	if (!added) {
		areas.push(new Area(id, calcPer(i, j)));
	}

	if (i + 1 < wid && map[i + 1][j] == map[i][j]) add(i + 1, j, id);
	if (i - 1 >= 0 && map[i - 1][j] == map[i][j]) add(i - 1, j, id);
	if (j + 1 < wid && map[i][j + 1] == map[i][j]) add(i, j + 1, id);
	if (j - 1 >= 0 && map[i][j - 1] == map[i][j]) add(i, j - 1, id);

	return true;
}

// walk
for (let i = 0; i < wid; i++) {
	for (let j = 0; j < wid; j++) {
		let char = map[i][j];
		add(i, j, -1);
	}
}

// calculate result
let price = 0;
for (let area of areas) {
	price += area.tiles.size * area.perimiter;
	area.price = area.tiles.size * area.perimiter;
}

console.log(price);
