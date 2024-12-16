const path = require("path");
const file = path.join(__dirname, "/14.txt");
const fs = require("node:fs");
const { verify } = require("crypto");

let data = fs.readFileSync(file, "utf8").split("\n");

let robots = [0, 0, 0, 0];
let seconds = 100;
let wid = 101;
//let wid = 11;
let hig = 103;
//let hig = 7;

for (let line of data) {
	line = line.split(" ");
	pos = line[0]
		.substring(2)
		.split(",")
		.map((a) => parseInt(a));
	vel = line[1]
		.substring(2)
		.split(",")
		.map((a) => parseInt(a));

	let xfin = (pos[0] + seconds * vel[0]) % wid;
	let yfin = (pos[1] + seconds * vel[1]) % hig;

	if (yfin < 0) yfin += hig;
	if (xfin < 0) xfin += wid;

	if (yfin == (hig - 1) / 2 || xfin == (wid - 1) / 2) continue;

	ir = 0 + +(yfin > (hig - 1) / 2) * 2 + +(xfin > (wid - 1) / 2);
	robots[ir] = robots[ir] + 1;
}

res = 1;
for (let r of robots) {
	res *= r;
}
console.log(res);

// 42409 too high
// 40463 not
