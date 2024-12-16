const path = require("path");
const file = path.join(__dirname, "/13.txt");
const fs = require("node:fs");

let data = fs.readFileSync(file, "utf8").split("\n");

let i = 0;
let coins = 0;

while (i < data.length) {
	console.log(i);
	let a = data[i].match(/\d+/g).map((a) => parseInt(a));
	let b = data[i + 1].match(/\d+/g).map((a) => parseInt(a));
	let prize = data[i + 2].match(/\d+/g).map((a) => parseInt(a));
	i += 4;
	console.log(a, b, prize);

	for (let k = 0; k <= 100; k++) {
		if (
			(prize[0] - k * a[0]) % b[0] == 0 &&
			(prize[1] - k * a[1]) % b[1] == 0 &&
			(prize[1] - k * a[1]) / b[1] <= 100 &&
			(prize[0] - k * a[0]) / b[0] == (prize[1] - k * a[1]) / b[1]
		) {
			console.log("MOVE", k, (prize[0] - k * a[0]) / b[0]);
			coins += 3 * k + (prize[0] - a[0] * k) / b[0];
			break;
		}
	}
	console.log(coins);
}
// 42409 too high
// 40463 not
console.log(coins);
